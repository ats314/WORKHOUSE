"""
TENSOR_NETWORK RAG Indexer
Builds a ChromaDB index from all markdown/text files in the TENSOR_NETWORK directory.
"""
import os
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
BASE_DIR = Path(__file__).parent.parent
CHROMA_DIR = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "tn_documents"

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Split text into overlapping chunks."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)
    return chunks

def load_documents():
    """Load all markdown and text files from TENSOR_NETWORK subdirectories."""
    documents = []
    metadatas = []
    ids = []
    
    doc_id = 0
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip tools and chroma_db directories
        rel_root = Path(root).relative_to(BASE_DIR)
        if any(skip in str(rel_root) for skip in ['tools', 'chroma_db', '__pycache__']):
            continue
            
        for file in files:
            if file.endswith(('.md', '.txt')):
                filepath = Path(root) / file
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                    
                    # Get relative path for metadata
                    rel_path = filepath.relative_to(BASE_DIR)
                    folder = str(rel_path.parent) if str(rel_path.parent) != '.' else 'ROOT'
                    
                    # Chunk the document
                    chunks = chunk_text(content)
                    
                    for i, chunk in enumerate(chunks):
                        documents.append(chunk)
                        metadatas.append({
                            "source": str(rel_path),
                            "folder": folder,
                            "filename": file,
                            "chunk": i
                        })
                        ids.append(f"doc_{doc_id}_{i}")
                    
                    doc_id += 1
                    print(f"  Loaded: {rel_path} ({len(chunks)} chunks)")
                    
                except Exception as e:
                    print(f"  ERROR loading {filepath}: {e}")
    
    return documents, metadatas, ids

def main():
    print("=" * 70)
    print("TENSOR_NETWORK RAG Indexer")
    print("=" * 70)
    
    # Initialize ChromaDB
    print(f"\nInitializing ChromaDB at: {CHROMA_DIR}")
    CHROMA_DIR.mkdir(exist_ok=True)
    
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    
    # Create embedding function
    print(f"Using embedding model: {EMBEDDING_MODEL}")
    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    
    # Delete existing collection if present
    try:
        client.delete_collection(COLLECTION_NAME)
        print(f"Deleted existing collection: {COLLECTION_NAME}")
    except:
        pass
    
    # Create new collection
    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_fn
    )
    
    # Load and index documents
    print(f"\nLoading documents from: {BASE_DIR}")
    documents, metadatas, ids = load_documents()
    
    if not documents:
        print("No documents found!")
        return
    
    print(f"\nIndexing {len(documents)} chunks...")
    
    # Add in batches
    batch_size = 100
    for i in range(0, len(documents), batch_size):
        batch_docs = documents[i:i + batch_size]
        batch_meta = metadatas[i:i + batch_size]
        batch_ids = ids[i:i + batch_size]
        
        collection.add(
            documents=batch_docs,
            metadatas=batch_meta,
            ids=batch_ids
        )
        print(f"  Indexed batch {i // batch_size + 1}/{(len(documents) - 1) // batch_size + 1}")
    
    print("\n" + "=" * 70)
    print(f"[OK] Indexing complete! {len(documents)} chunks indexed.")
    print(f"Database location: {CHROMA_DIR}")
    print("=" * 70)

if __name__ == "__main__":
    main()
