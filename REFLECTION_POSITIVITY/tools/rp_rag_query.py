#!/usr/bin/env python3
"""
REFLECTION_POSITIVITY RAG System - Query Interface

Usage:
    python rp_rag_query.py "your search query"

Examples:
    python rp_rag_query.py "Osterwalder-Schrader reconstruction"
    python rp_rag_query.py "reflection positivity permanence"
    python rp_rag_query.py "spectral gap to mass gap"
"""

import os
import sys
import io
from pathlib import Path

# Fix encoding for Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

try:
    import chromadb
except ImportError:
    print("Installing chromadb...")
    os.system("pip install chromadb")
    import chromadb

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Installing sentence-transformers...")
    os.system("pip install sentence-transformers")
    from sentence_transformers import SentenceTransformer

# Configuration
DB_PATH = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "rp_documents"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def sanitize_text(text):
    """Replace problematic Unicode characters with ASCII equivalents."""
    replacements = {
        '\u2192': '->',  # →
        '\u2190': '<-',  # ←
        '\u2194': '<->',  # ↔
        '\u2713': '[OK]',  # ✓
        '\u2717': '[X]',  # ✗
        '\u2022': '-',  # •
        '\u2026': '...',  # …
        '\u03b1': 'alpha',  # α
        '\u03b2': 'beta',  # β
        '\u03b3': 'gamma',  # γ
        '\u03bb': 'lambda',  # λ
        '\u03bc': 'mu',  # μ
        '\u03c1': 'rho',  # ρ
        '\u03c3': 'sigma',  # σ
        '\u2264': '<=',  # ≤
        '\u2265': '>=',  # ≥
        '\u221e': 'inf',  # ∞
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text


def query(query_text: str, n_results: int = 5):
    """Search the REFLECTION_POSITIVITY RAG index."""
    if not DB_PATH.exists():
        print("Error: Database not found. Run 'python rp_rag_index.py' first.")
        return
    
    model = SentenceTransformer(EMBEDDING_MODEL)
    query_embedding = model.encode([query_text])[0]
    
    client = chromadb.PersistentClient(path=str(DB_PATH))
    collection = client.get_collection(name=COLLECTION_NAME)
    
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )
    
    print("=" * 70)
    print(f"REFLECTION_POSITIVITY RAG - Query: '{query_text}'")
    print("=" * 70)
    print(f"Found {len(results['ids'][0])} results")
    print("=" * 70)
    
    for i, (doc_id, document, metadata, distance) in enumerate(zip(
        results['ids'][0], 
        results['documents'][0], 
        results['metadatas'][0],
        results['distances'][0]
    )):
        relevance = (1 - distance) * 100
        folder = metadata.get('folder', 'unknown')
        filename = metadata.get('filename', doc_id)
        
        snippet = sanitize_text(document[:400].replace('\n', ' ').strip())
        if len(document) > 400:
            snippet += "..."
        
        print(f"\n[{i+1}] Relevance: {relevance:.1f}%")
        print(f"    {folder} / {filename}")
        print(f"    {snippet}")
        print("-" * 70)
    
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rp_rag_query.py \"your search query\"")
        print("\nExamples:")
        print("  python rp_rag_query.py \"Osterwalder-Schrader axioms\"")
        print("  python rp_rag_query.py \"reflection positivity permanence\"")
        print("  python rp_rag_query.py \"diffusion to mass gap bridge\"")
        sys.exit(1)
    
    query_text = " ".join(sys.argv[1:])
    query(query_text)
