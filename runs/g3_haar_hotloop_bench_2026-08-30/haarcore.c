/* Exact set-partition merge: the hot loop of the O(u^4) Haar contraction.
 *
 * G3's live route is one cross-plane amplitude, and the register measured the
 * wall precisely: a pure-Python union-find/canon inner loop that is 81% of
 * the cumulative time of an exact Haar inner product, called 350k+ times for
 * a single degree-3 Gram entry. That is arithmetic-free bookkeeping -- build
 * a parent array, union by first label occurrence, union the Weingarten
 * pairs, relabel canonically -- so it belongs in C, and nothing about the
 * mathematics changes by moving it.
 *
 * This is an OPTIONAL accelerator. workhouse.haar_exact falls back to a pure
 * Python implementation with identical output when the extension is absent,
 * so no platform needs a compiler and the CI matrix is unchanged.
 */

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define STACK_SLOTS 256

static inline int uf_find(int *parent, int i) {
    while (parent[i] != i) {
        parent[i] = parent[parent[i]];   /* path halving */
        i = parent[i];
    }
    return i;
}

static inline void uf_union(int *parent, int a, int b) {
    int ra = uf_find(parent, a), rb = uf_find(parent, b);
    if (ra != rb) parent[rb] = ra;       /* left root wins: matches the
                                          * reference implementation, which
                                          * canonicalises afterwards anyway */
}

/* merge_classes(partition, pairs) -> canonical tuple
 *
 * partition: sequence of non-negative ints (the current colour partition)
 * pairs:     sequence of (i, j) index pairs, the exact Kronecker deltas
 */
static PyObject *merge_classes(PyObject *self, PyObject *args) {
    PyObject *part_obj, *pairs_obj;
    if (!PyArg_ParseTuple(args, "OO", &part_obj, &pairs_obj)) return NULL;

    PyObject *part_seq = PySequence_Fast(part_obj, "partition must be a sequence");
    if (!part_seq) return NULL;
    Py_ssize_t size = PySequence_Fast_GET_SIZE(part_seq);
    PyObject **items = PySequence_Fast_ITEMS(part_seq);

    int stack_parent[STACK_SLOTS], stack_label[STACK_SLOTS], stack_first[STACK_SLOTS];
    int *parent = stack_parent, *label = stack_label, *first = stack_first;
    int heap = size > STACK_SLOTS;
    if (heap) {
        parent = (int *)PyMem_Malloc(sizeof(int) * (size_t)size * 3);
        if (!parent) { Py_DECREF(part_seq); return PyErr_NoMemory(); }
        label = parent + size;
        first = label + size;
    }

    /* Labels are small non-negative ints; `first` doubles as a label ->
     * first-slot table, so the reference implementation's dict disappears. */
    int max_label = -1;
    for (Py_ssize_t i = 0; i < size; i++) {
        long v = PyLong_AsLong(items[i]);
        if (v == -1 && PyErr_Occurred()) goto fail;
        if (v < 0) { PyErr_SetString(PyExc_ValueError, "labels must be >= 0"); goto fail; }
        label[i] = (int)v;
        if ((int)v > max_label) max_label = (int)v;
        parent[i] = (int)i;
    }
    if (max_label >= size) {
        /* first[] is indexed by label, so labels must fit; canonical inputs
         * always satisfy this, but a caller could pass a sparse partition. */
        PyErr_SetString(PyExc_ValueError, "partition labels must be < len(partition)");
        goto fail;
    }
    for (int l = 0; l <= max_label; l++) first[l] = -1;
    for (Py_ssize_t i = 0; i < size; i++) {
        int l = label[i];
        if (first[l] < 0) first[l] = (int)i;
        else uf_union(parent, (int)i, first[l]);
    }

    PyObject *pairs_seq = PySequence_Fast(pairs_obj, "pairs must be a sequence");
    if (!pairs_seq) goto fail;
    Py_ssize_t npairs = PySequence_Fast_GET_SIZE(pairs_seq);
    PyObject **pair_items = PySequence_Fast_ITEMS(pairs_seq);
    for (Py_ssize_t k = 0; k < npairs; k++) {
        PyObject *pair = PySequence_Fast(pair_items[k], "each pair must be a sequence");
        if (!pair) { Py_DECREF(pairs_seq); goto fail; }
        if (PySequence_Fast_GET_SIZE(pair) != 2) {
            Py_DECREF(pair); Py_DECREF(pairs_seq);
            PyErr_SetString(PyExc_ValueError, "each pair must have length 2");
            goto fail;
        }
        PyObject **pv = PySequence_Fast_ITEMS(pair);
        long a = PyLong_AsLong(pv[0]), b = PyLong_AsLong(pv[1]);
        Py_DECREF(pair);
        if ((a == -1 || b == -1) && PyErr_Occurred()) { Py_DECREF(pairs_seq); goto fail; }
        if (a < 0 || a >= size || b < 0 || b >= size) {
            Py_DECREF(pairs_seq);
            PyErr_SetString(PyExc_IndexError, "pair index out of range");
            goto fail;
        }
        uf_union(parent, (int)a, (int)b);
    }
    Py_DECREF(pairs_seq);

    /* Canonicalise by first occurrence, reusing `label` as root -> new-label. */
    for (Py_ssize_t i = 0; i < size; i++) label[i] = -1;
    PyObject *out = PyTuple_New(size);
    if (!out) goto fail;
    int next = 0;
    for (Py_ssize_t i = 0; i < size; i++) {
        int root = uf_find(parent, (int)i);
        if (label[root] < 0) label[root] = next++;
        PyObject *num = PyLong_FromLong(label[root]);
        if (!num) { Py_DECREF(out); goto fail; }
        PyTuple_SET_ITEM(out, i, num);
    }
    if (heap) PyMem_Free(parent);
    Py_DECREF(part_seq);
    return out;

fail:
    if (heap) PyMem_Free(parent);
    Py_DECREF(part_seq);
    return NULL;
}

static PyMethodDef methods[] = {
    {"merge_classes", merge_classes, METH_VARARGS,
     "merge_classes(partition, pairs) -> canonical tuple of ints"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT, "_haarcore",
    "Compiled inner loop for the exact Haar set-partition contraction.",
    -1, methods, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit__haarcore(void) { return PyModule_Create(&moduledef); }
