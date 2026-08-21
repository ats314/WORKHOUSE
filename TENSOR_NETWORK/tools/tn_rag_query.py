"""
TENSOR_NETWORK RAG Query Tool
Semantic search over indexed TENSOR_NETWORK documents.
"""
import sys
from pathlib import Path

# Force UTF-8 encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import chromadb
from chromadb.utils import embedding_functions

# Configuration
CHROMA_DIR = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "tn_documents"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

def sanitize_text(text: str) -> str:
    """Replace problematic Unicode characters with ASCII equivalents."""
    replacements = {
        '\u2192': '->',  # →
        '\u2190': '<-',  # ←
        '\u2194': '<->',  # ↔
        '\u21d2': '=>',  # ⇒
        '\u21d0': '<=',  # ⇐
        '\u2265': '>=',  # ≥
        '\u2264': '<=',  # ≤
        '\u2260': '!=',  # ≠
        '\u221e': 'inf',  # ∞
        '\u2211': 'sum',  # ∑
        '\u220f': 'prod',  # ∏
        '\u222b': 'int',  # ∫
        '\u2202': 'd',  # ∂
        '\u2207': 'nabla',  # ∇
        '\u03b1': 'alpha',  # α
        '\u03b2': 'beta',  # β
        '\u03b3': 'gamma',  # γ
        '\u03b4': 'delta',  # δ
        '\u03b5': 'epsilon',  # ε
        '\u03bb': 'lambda',  # λ
        '\u03bc': 'mu',  # μ
        '\u03c0': 'pi',  # π
        '\u03c3': 'sigma',  # σ
        '\u03c4': 'tau',  # τ
        '\u03c9': 'omega',  # ω
        '\u2713': '[OK]',  # ✓
        '\u2717': '[X]',  # ✗
        '\u2022': '*',  # •
        '\u25cf': '*',  # ●
    }
    for unicode_char, ascii_replacement in replacements.items():
        text = text.replace(unicode_char, ascii_replacement)
    return text

def query(query_text: str, n_results: int = 5):
    """Query the TENSOR_NETWORK document index."""
    
    # Initialize ChromaDB
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    
    try:
        collection = client.get_collection(
            name=COLLECTION_NAME,
            embedding_function=embedding_fn
        )
    except Exception as e:
        print(f"ERROR: Collection not found. Run tn_rag_index.py first.")
        print(f"Details: {e}")
        return
    
    # Query
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    
    # Display results
    print("=" * 70)
    print(f"TENSOR_NETWORK RAG - Query: '{query_text}'")
    print("=" * 70)
    print(f"Found {len(results['documents'][0])} results")
    print("=" * 70)
    
    for i, (doc, meta, distance) in enumerate(zip(
        results['documents'][0],
        results['metadatas'][0],
        results['distances'][0]
    )):
        relevance = (1 - distance) * 100
        print(f"\n[{i+1}] Relevance: {relevance:.1f}%")
        print(f"    {meta['folder']} / {meta['filename']}")
        
        # Truncate and sanitize document preview
        preview = doc[:300] + "..." if len(doc) > 300 else doc
        preview = sanitize_text(preview)
        print(f"    {preview}")
        print("-" * 70)

def main():
    if len(sys.argv) < 2:
        print("Usage: python tn_rag_query.py <query>")
        print("Example: python tn_rag_query.py 'q-Racah mass gap'")
        return
    
    query_text = " ".join(sys.argv[1:])
    query(query_text)

if __name__ == "__main__":
    main()
