#!/usr/bin/env python3
"""
REFLECTION_POSITIVITY RAG System - Embedding and Indexing

Usage:
    python rp_rag_index.py

This script embeds all markdown files in the REFLECTION_POSITIVITY folder 
and stores them in a local ChromaDB vector database for semantic search.
"""

import os
import sys
from pathlib import Path
from typing import List, Dict

# Check for required packages
try:
    import chromadb
    from chromadb.config import Settings
except ImportError:
    print("Installing chromadb...")
    os.system("pip install chromadb")
    import chromadb
    from chromadb.config import Settings

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("Installing sentence-transformers...")
    os.system("pip install sentence-transformers")
    from sentence_transformers import SentenceTransformer

# Configuration
RP_PATH = Path(__file__).parent.parent  # REFLECTION_POSITIVITY folder
DB_PATH = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "rp_documents"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def load_documents(base_path: Path) -> List[Dict]:
    """Load all markdown files from REFLECTION_POSITIVITY folder and subfolders."""
    documents = []
    
    for md_file in base_path.rglob("*.md"):
        if "tools" in str(md_file):
            continue
            
        try:
            content = md_file.read_text(encoding="utf-8", errors="ignore")
            if len(content) < 100:
                continue
            
            folder = md_file.parent.name if md_file.parent != base_path else "root"
            
            documents.append({
                "id": str(md_file.relative_to(base_path)),
                "content": content,
                "metadata": {
                    "filename": md_file.name,
                    "folder": folder,
                    "path": str(md_file),
                    "size": len(content)
                }
            })
            print(f"  Loaded: {md_file.name} ({len(content):,} chars)")
            
        except Exception as e:
            print(f"  Error loading {md_file}: {e}")
    
    # Also load .txt files
    for txt_file in base_path.rglob("*.txt"):
        if "tools" in str(txt_file):
            continue
            
        try:
            content = txt_file.read_text(encoding="utf-8", errors="ignore")
            if len(content) < 100:
                continue
            
            folder = txt_file.parent.name if txt_file.parent != base_path else "root"
            
            documents.append({
                "id": str(txt_file.relative_to(base_path)),
                "content": content,
                "metadata": {
                    "filename": txt_file.name,
                    "folder": folder,
                    "path": str(txt_file),
                    "size": len(content)
                }
            })
            print(f"  Loaded: {txt_file.name} ({len(content):,} chars)")
            
        except Exception as e:
            print(f"  Error loading {txt_file}: {e}")
    
    return documents


def chunk_document(doc: Dict, chunk_size: int = 1500, overlap: int = 200) -> List[Dict]:
    """Split document into overlapping chunks."""
    content = doc["content"]
    chunks = []
    paragraphs = content.split("\n\n")
    current_chunk = ""
    chunk_idx = 0
    
    for para in paragraphs:
        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append({
                    "id": f"{doc['id']}::chunk_{chunk_idx}",
                    "content": current_chunk.strip(),
                    "metadata": {**doc["metadata"], "chunk_index": chunk_idx, "source_doc": doc["id"]}
                })
                chunk_idx += 1
            words = current_chunk.split()
            overlap_text = " ".join(words[-50:]) if len(words) > 50 else ""
            current_chunk = overlap_text + "\n\n" + para + "\n\n"
    
    if current_chunk.strip():
        chunks.append({
            "id": f"{doc['id']}::chunk_{chunk_idx}",
            "content": current_chunk.strip(),
            "metadata": {**doc["metadata"], "chunk_index": chunk_idx, "source_doc": doc["id"]}
        })
    
    return chunks


def build_index():
    """Build the ChromaDB index from REFLECTION_POSITIVITY documents."""
    print("=" * 60)
    print("REFLECTION_POSITIVITY RAG System - Indexing")
    print("=" * 60)
    
    print(f"\n[*] Loading embedding model: {EMBEDDING_MODEL}")
    model = SentenceTransformer(EMBEDDING_MODEL)
    print("    Model loaded!")
    
    print(f"\n[*] Loading documents from: {RP_PATH}")
    documents = load_documents(RP_PATH)
    print(f"    Loaded {len(documents)} documents")
    
    print("\n[*] Chunking documents...")
    all_chunks = []
    for doc in documents:
        chunks = chunk_document(doc)
        all_chunks.extend(chunks)
    print(f"    Created {len(all_chunks)} chunks")
    
    print("\n[*] Creating embeddings...")
    texts = [chunk["content"] for chunk in all_chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    print(f"    Created {len(embeddings)} embeddings")
    
    print(f"\n[*] Saving to ChromaDB: {DB_PATH}")
    DB_PATH.mkdir(exist_ok=True)
    client = chromadb.PersistentClient(path=str(DB_PATH))
    
    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass
    
    collection = client.create_collection(name=COLLECTION_NAME)
    collection.add(
        ids=[chunk["id"] for chunk in all_chunks],
        embeddings=embeddings.tolist(),
        documents=[chunk["content"] for chunk in all_chunks],
        metadatas=[chunk["metadata"] for chunk in all_chunks]
    )
    
    print(f"    Indexed {len(all_chunks)} chunks!")
    print("\n" + "=" * 60)
    print("[OK] REFLECTION_POSITIVITY RAG Index Built Successfully!")
    print("=" * 60)
    print(f"    Documents: {len(documents)}")
    print(f"    Chunks: {len(all_chunks)}")
    print(f"    Database: {DB_PATH}")
    print("\nRun 'python rp_rag_query.py' to search")


if __name__ == "__main__":
    build_index()
