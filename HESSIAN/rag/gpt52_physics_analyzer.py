#!/usr/bin/env python3
"""
GPT-5.2 Physics RAG Analyzer - v2.0
====================================================
Uses GPT-5.2 with OpenAI embeddings to analyze physics synthesis documents.

IMPROVEMENTS IN V2:
- Added 'critical-path' analysis type for focused gap identification
- Added 'fixes' analysis type to get concrete fix proposals
- Added cost tracking and token reporting
- Added severity summaries at top of reports
- Added multi-document analysis support
- Improved prompts based on v1 learnings

USAGE:
    python gpt52_physics_analyzer.py analyze Synthesis_15.md --type contradictions
    python gpt52_physics_analyzer.py analyze Synthesis_15.md --type critical-path
    python gpt52_physics_analyzer.py analyze Synthesis_15.md --type fixes
    python gpt52_physics_analyzer.py analyze-all --type contradictions
    python gpt52_physics_analyzer.py build-index
"""

import os
import sys
import json
import pickle
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
import re
from datetime import datetime

# ============================================================================
# PATH CONFIGURATION (Auto-detect from script location)
# ============================================================================
SCRIPT_DIR = Path(__file__).parent
SUBJECT_DIR = SCRIPT_DIR.parent  # This is the subject folder (e.g., HAAR)
FOLDER_NAME = SUBJECT_DIR.name
PROJECT_ROOT = SUBJECT_DIR.parent  # proof/

# Subject-specific paths
SYNTHESIS_DIR = SUBJECT_DIR / "MODEL_CREATION"
SOURCE_DIR = SUBJECT_DIR

# Output files
GPT52_INDEX_FILE = SCRIPT_DIR / f"{FOLDER_NAME.lower()}_gpt52_index.pkl"
ANALYSIS_OUTPUT_DIR = SUBJECT_DIR / "analysis_reports"
# Available subject folders
SUBJECT_FOLDERS = [
    "HAAR", "WILSON", "HESSIAN", "LSI_POINCARE", "RICCATI", "RG_COARSE",
    "HELFFER_SJOSTRAND", "COMBES_THOMAS", "LYAPUNOV", "REFLECTION_POSITIVITY",
    "MAXWELL", "POLARITY_GRIBOV", "SCALING_LIMIT", "SIMULATIONS", "TENSOR_NETWORK",
    "UNIFORMITY_ASYMPTOTIC_FREEDOM", "VSU_COSMOLOGY"
]

def resolve_topic_paths(topic: str):
    """
    Resolve synthesis doc, RAG index, and output dir for any subject folder.
    Returns: (synthesis_path, rag_index_path, output_dir) or raises error.
    """
    topic_dir = PROJECT_ROOT / topic
    if not topic_dir.exists():
        # Try case-insensitive match
        for folder in SUBJECT_FOLDERS:
            if folder.lower() == topic.lower():
                topic_dir = PROJECT_ROOT / folder
                break
    
    if not topic_dir.exists():
        raise FileNotFoundError(f"Subject folder not found: {topic}")
    
    # Find synthesis document (check common locations)
    synthesis_candidates = list(topic_dir.rglob("Synthesis_*.md"))
    if not synthesis_candidates:
        raise FileNotFoundError(f"No Synthesis_*.md found in {topic}")
    synthesis_path = synthesis_candidates[0]
    
    # Find existing RAG index in the folder
    rag_dir = topic_dir / "rag"
    rag_index_path = None
    if rag_dir.exists():
        index_candidates = list(rag_dir.glob("*_index.pkl"))
        if index_candidates:
            rag_index_path = index_candidates[0]
    
    # Output directory in the subject folder
    output_dir = topic_dir / "analysis_reports"
    
    return synthesis_path, rag_index_path, output_dir

# ============================================================================
# OPENAI CONFIGURATION
# ============================================================================
GPT52_MODEL = "gpt-5.2"  # Or "gpt-5.2-thinking" for complex reasoning
EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_DIMENSIONS = 3072  # text-embedding-3-large

# Token limits
MAX_CONTEXT_TOKENS = 400_000
MAX_OUTPUT_TOKENS = 16_000  # Reasonable for analysis reports

# Pricing (per 1K tokens) - GPT-5.2 estimated
PRICING = {
    "gpt-5.2": {"input": 0.005, "output": 0.015},
    "text-embedding-3-large": {"input": 0.00013},
}

# ============================================================================
# DEPENDENCIES
# ============================================================================
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("WARNING: numpy not installed. Some features will be limited.")

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("WARNING: openai not installed. Install with: pip install openai>=1.50.0")

try:
    import ollama
    HAS_OLLAMA = True
except ImportError:
    HAS_OLLAMA = False
    print("WARNING: ollama not installed. Install with: pip install ollama")

# ============================================================================
# LOCAL MODEL CONFIGURATION
# ============================================================================
LOCAL_MODELS = {
    "fast": "phi4-mini",           # Quick screening, ~3s
    "math": "qwen2-math:7b",       # Math verification, ~5s
    "reasoning": "deepseek-r1:14b", # Chain-of-thought, ~30s
}

# Cloud model tiers
CLOUD_MODELS = {
    "nano": "gpt-4o-mini",  # Cheap screening (~$0.01)
    "full": "gpt-5.2",      # Deep analysis (~$0.15)
}

# ============================================================================
# DATA CLASSES
# ============================================================================
@dataclass
class Chunk:
    """A document chunk for embedding."""
    id: int
    content: str
    source_file: str
    section: str
    metadata: Dict[str, Any]

@dataclass
class TokenUsage:
    """Track token usage for cost estimation."""
    input_tokens: int = 0
    output_tokens: int = 0
    embedding_tokens: int = 0
    
    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens + self.embedding_tokens
    
    @property
    def estimated_cost(self) -> float:
        """Estimate cost in USD."""
        input_cost = (self.input_tokens / 1000) * PRICING["gpt-5.2"]["input"]
        output_cost = (self.output_tokens / 1000) * PRICING["gpt-5.2"]["output"]
        embed_cost = (self.embedding_tokens / 1000) * PRICING["text-embedding-3-large"]["input"]
        return input_cost + output_cost + embed_cost

@dataclass
class AnalysisResult:
    """Result from GPT-5.2 analysis."""
    analysis_type: str
    document: str
    raw_response: str
    usage: TokenUsage = field(default_factory=TokenUsage)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    severity_counts: Dict[str, int] = field(default_factory=dict)

# ============================================================================
# OPENAI CLIENT
# ============================================================================
def get_openai_client() -> Optional["OpenAI"]:
    """Get OpenAI client with API key from project .env file (same as startup swarm)."""
    if not HAS_OPENAI:
        return None
    
    # Load from project .env file (same location as startup swarm uses)
    try:
        from dotenv import load_dotenv
        env_path = PROJECT_ROOT / ".env"
        if env_path.exists():
            load_dotenv(env_path)
            print(f"Loaded API keys from: {env_path}")
    except ImportError:
        print("WARNING: python-dotenv not installed. Install with: pip install python-dotenv")
    
    # Get API key - support swarm key pool for higher concurrency
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Check for swarm key pool (multiple keys for parallel requests)
    swarm_keys = os.environ.get("OPENAI_SWARM_KEYS")
    if swarm_keys:
        import random
        keys = [k.strip() for k in swarm_keys.split(",") if k.strip()]
        if keys:
            api_key = random.choice(keys)
            print(f"Using swarm key: ...{api_key[-4:]}")
    
    if not api_key:
        print("ERROR: OPENAI_API_KEY not found in .env file")
        print(f"Expected .env location: {PROJECT_ROOT / '.env'}")
        return None
    
    return OpenAI(api_key=api_key)

# ============================================================================
# LOCAL MODEL FUNCTIONS (OLLAMA)
# ============================================================================
def check_ollama_available() -> bool:
    """Check if Ollama is running and has required models."""
    if not HAS_OLLAMA:
        return False
    try:
        response = ollama.list()
        # Handle both dict and object response formats
        if hasattr(response, 'models'):
            models_list = response.models
        else:
            models_list = response.get('models', [])
        
        available = []
        for m in models_list:
            name = m.model if hasattr(m, 'model') else m.get('name', '')
            available.append(name.split(':')[0])
        
        required = ['phi4-mini', 'qwen2-math', 'deepseek-r1']
        missing = [m for m in required if not any(m in a for a in available)]
        if missing:
            print(f"WARNING: Missing local models: {missing}")
        return True
    except Exception as e:
        print(f"WARNING: Ollama not available: {e}")
        return False

def local_screen_equations(document: str, model: str = "phi4-mini") -> Dict[str, Any]:
    """Extract and validate equations using local model."""
    if not HAS_OLLAMA:
        return {"error": "Ollama not installed"}
    
    prompt = """Extract all mathematical equations from this document.
For each equation, output JSON with:
- equation: the LaTeX
- location: chapter/section reference
- symbols: list of symbols used

Focus on finding:
1. Riccati equations (λ̇ = ...)
2. Fixed point definitions (λ* = ...)
3. Bound definitions (ρ, σ, etc.)

Return valid JSON array."""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": f"{prompt}\n\nDocument:\n{document[:15000]}"}]
        )
        return {
            "model": model,
            "response": response['message']['content'],
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e), "status": "failed"}

def local_verify_math(claim: str, model: str = "qwen2-math:7b", rag_context: str = None) -> Dict[str, Any]:
    """Verify a mathematical claim using the math-specialized model with optional RAG context."""
    if not HAS_OLLAMA:
        return {"error": "Ollama not installed"}
    
    # Build prompt with or without RAG context
    if rag_context:
        prompt = f"""You are verifying a mathematical claim from a physics document.

## Retrieved Source Material
{rag_context}

## Claim to Verify
{claim}

## Instructions
1. Check if this claim is supported by the source material above
2. Work through the math step by step
3. Check for algebraic errors
4. State TRUE if mathematically correct and supported, FALSE if wrong or unsupported, UNCLEAR if insufficient evidence

Answer TRUE, FALSE, or UNCLEAR on the first line, then explain your reasoning."""
    else:
        prompt = f"""Is this mathematical claim correct? 
Claim: {claim}

1. Work through the math step by step
2. Check for algebraic errors
3. State TRUE or FALSE with justification"""
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        content = response['message']['content']
        # Extract verdict from first line
        first_line = content.split('\n')[0].upper()
        if "TRUE" in first_line:
            verdict = "TRUE"
        elif "FALSE" in first_line:
            verdict = "FALSE"
        else:
            verdict = "UNCLEAR"
        return {
            "model": model,
            "verdict": verdict,
            "reasoning": content,
            "has_rag_context": rag_context is not None,
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e), "status": "failed"}

def local_deep_reasoning(question: str, model: str = "deepseek-r1:14b") -> Dict[str, Any]:
    """Use DeepSeek-R1 for chain-of-thought reasoning on complex questions."""
    if not HAS_OLLAMA:
        return {"error": "Ollama not installed"}
    
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": question}]
        )
        return {
            "model": model,
            "response": response['message']['content'],
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e), "status": "failed"}

def ensemble_check(claim: str, rag_context: str = None) -> Dict[str, Any]:
    """
    Check a claim with multiple local models to detect disagreements.
    Uses RAG context when available for evidence-based verification.
    Disagreement = signal for human review.
    """
    if not HAS_OLLAMA:
        return {"error": "Ollama not installed"}
    
    models = ["phi4-mini", "qwen2-math:7b", "deepseek-r1:14b"]
    results = {}
    verdicts = []
    
    # Build prompt with or without RAG context
    if rag_context:
        prompt = f"""You are verifying a claim from a physics document against source material.

## Retrieved Source Material
{rag_context}

## Claim to Verify
{claim}

## Instructions
1. Check if this claim is mathematically correct
2. Check if the claim is supported by the source material
3. Answer TRUE if correct and supported, FALSE if wrong or contradicted, UNCLEAR if insufficient evidence

Answer TRUE, FALSE, or UNCLEAR on the first line, then explain your reasoning."""
    else:
        prompt = f"""Is this claim mathematically correct? Answer TRUE or FALSE on the first line, then explain.

Claim: {claim}"""
    
    for model in models:
        try:
            response = ollama.chat(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response['message']['content']
            # Extract verdict from first line
            first_line = content.split('\n')[0].upper()
            if "TRUE" in first_line:
                verdict = "TRUE"
            elif "FALSE" in first_line:
                verdict = "FALSE"
            else:
                verdict = "UNCLEAR"
            
            results[model] = {
                "verdict": verdict,
                "reasoning": content[:500]
            }
            verdicts.append(verdict)
        except Exception as e:
            results[model] = {"error": str(e)}
    
    # Check for disagreement
    unique_verdicts = set(v for v in verdicts if v != "UNCLEAR")
    
    return {
        "claim": claim,
        "results": results,
        "consensus": len(unique_verdicts) <= 1,
        "verdict": list(unique_verdicts)[0] if len(unique_verdicts) == 1 else "DISAGREEMENT",
        "requires_human": len(unique_verdicts) > 1,
        "has_rag_context": rag_context is not None
    }

# ============================================================================
# EMBEDDING FUNCTIONS
# ============================================================================
def embed_text(client: "OpenAI", text: str) -> Tuple[List[float], int]:
    """Embed text using OpenAI's text-embedding-3-large. Returns (embedding, tokens)."""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
        dimensions=EMBEDDING_DIMENSIONS
    )
    return response.data[0].embedding, response.usage.total_tokens

def embed_batch(client: "OpenAI", texts: List[str], batch_size: int = 100) -> Tuple[List[List[float]], int]:
    """Embed a batch of texts. Returns (embeddings, total_tokens)."""
    all_embeddings = []
    total_tokens = 0
    
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=batch,
            dimensions=EMBEDDING_DIMENSIONS
        )
        batch_embeddings = [item.embedding for item in response.data]
        all_embeddings.extend(batch_embeddings)
        total_tokens += response.usage.total_tokens
        print(f"  Embedded {min(i + batch_size, len(texts))}/{len(texts)} chunks ({total_tokens:,} tokens)")
    
    return all_embeddings, total_tokens

def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not HAS_NUMPY:
        # Pure Python fallback
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = sum(x * x for x in a) ** 0.5
        norm_b = sum(x * x for x in b) ** 0.5
        return dot / (norm_a * norm_b + 1e-10)
    else:
        a_np = np.array(a)
        b_np = np.array(b)
        return float(np.dot(a_np, b_np) / (np.linalg.norm(a_np) * np.linalg.norm(b_np) + 1e-10))

# ============================================================================
# DOCUMENT PARSING
# ============================================================================
def parse_markdown_sections(text: str, source_file: str) -> List[Chunk]:
    """Parse markdown document into chunks by section."""
    chunks = []
    
    # Split by headers
    section_pattern = r'^(#{1,4})\s+(.+)$'
    lines = text.split('\n')
    
    current_section = "Introduction"
    current_content = []
    chunk_id = 0
    
    for line in lines:
        match = re.match(section_pattern, line)
        if match:
            # Save previous section if it has content
            if current_content:
                content = '\n'.join(current_content).strip()
                if len(content) > 50:  # Minimum content threshold
                    chunks.append(Chunk(
                        id=chunk_id,
                        content=content,
                        source_file=source_file,
                        section=current_section,
                        metadata={'header_level': len(match.group(1))}
                    ))
                    chunk_id += 1
            
            current_section = match.group(2).strip()
            current_content = [line]
        else:
            current_content.append(line)
    
    # Don't forget the last section
    if current_content:
        content = '\n'.join(current_content).strip()
        if len(content) > 50:
            chunks.append(Chunk(
                id=chunk_id,
                content=content,
                source_file=source_file,
                section=current_section,
                metadata={}
            ))
    
    return chunks

def collect_source_documents(source_dir: Path) -> List[Tuple[Path, str]]:
    """Collect all source markdown documents."""
    documents = []
    exclude_dirs = {'rag', 'archive', '__pycache__', '.git', 'DUPLICATES'}
    
    for path in source_dir.rglob('*.md'):
        # Skip excluded directories
        if any(ex in str(path) for ex in exclude_dirs):
            continue
        
        try:
            content = path.read_text(encoding='utf-8')
            documents.append((path, content))
        except Exception as e:
            print(f"  Warning: Could not read {path}: {e}")
    
    return documents

# ============================================================================
# INDEX BUILDING
# ============================================================================
def build_openai_index(force_rebuild: bool = False) -> Dict[str, Any]:
    """Build or load OpenAI embedding index for POLARITY_GRIBOV documents."""
    
    if GPT52_INDEX_FILE.exists() and not force_rebuild:
        print(f"Loading existing index from {GPT52_INDEX_FILE}")
        with open(GPT52_INDEX_FILE, 'rb') as f:
            return pickle.load(f)
    
    print("Building new OpenAI embedding index...")
    
    client = get_openai_client()
    if not client:
        print("ERROR: Cannot build index without OpenAI client")
        return {}
    
    # Collect all documents
    print(f"Scanning {SOURCE_DIR} for documents...")
    documents = collect_source_documents(SOURCE_DIR)
    print(f"Found {len(documents)} documents")
    
    # Parse into chunks
    all_chunks = []
    for doc_path, content in documents:
        rel_path = doc_path.relative_to(SOURCE_DIR)
        chunks = parse_markdown_sections(content, str(rel_path))
        all_chunks.extend(chunks)
    
    print(f"Parsed into {len(all_chunks)} chunks")
    
    # Create embeddings
    print("Creating OpenAI embeddings...")
    chunk_texts = [f"{c.section}\n\n{c.content}" for c in all_chunks]
    embeddings, total_tokens = embed_batch(client, chunk_texts)
    
    # Estimate cost
    embed_cost = (total_tokens / 1000) * PRICING["text-embedding-3-large"]["input"]
    print(f"Embedding cost: ${embed_cost:.4f} ({total_tokens:,} tokens)")
    
    # Build index
    index = {
        'chunks': [
            {
                'id': c.id,
                'content': c.content,
                'source': c.source_file,
                'section': c.section,
                'metadata': c.metadata
            }
            for c in all_chunks
        ],
        'embeddings': embeddings,
        'model': EMBEDDING_MODEL,
        'dimensions': EMBEDDING_DIMENSIONS,
        'version': '2.0-gpt52',
        'build_tokens': total_tokens,
    }
    
    # Save
    SCRIPT_DIR.mkdir(parents=True, exist_ok=True)
    with open(GPT52_INDEX_FILE, 'wb') as f:
        pickle.dump(index, f)
    
    print(f"Index saved to {GPT52_INDEX_FILE}")
    return index

def build_topic_index(topic: str, force_rebuild: bool = False) -> Dict[str, Any]:
    """Build OpenAI embedding index for a specific subject folder."""
    
    # Resolve topic directory
    topic_dir = PROJECT_ROOT / topic
    if not topic_dir.exists():
        # Try case-insensitive match
        for folder in SUBJECT_FOLDERS:
            if folder.lower() == topic.lower():
                topic_dir = PROJECT_ROOT / folder
                topic = folder  # Use canonical name
                break
    
    if not topic_dir.exists():
        print(f"ERROR: Subject folder not found: {topic}")
        return {}
    
    # Output path in the topic's rag folder
    rag_dir = topic_dir / "rag"
    rag_dir.mkdir(parents=True, exist_ok=True)
    index_file = rag_dir / f"{topic.lower()}_gpt52_index.pkl"
    
    if index_file.exists() and not force_rebuild:
        print(f"Loading existing GPT-5.2 index from {index_file}")
        with open(index_file, 'rb') as f:
            return pickle.load(f)
    
    print(f"Building GPT-5.2 index for {topic}...")
    
    client = get_openai_client()
    if not client:
        print("ERROR: Cannot build index without OpenAI client")
        return {}
    
    # Collect documents from topic folder
    print(f"Scanning {topic_dir} for documents...")
    documents = collect_source_documents(topic_dir)
    print(f"Found {len(documents)} documents")
    
    if not documents:
        print(f"WARNING: No documents found in {topic_dir}")
        return {}
    
    # Parse into chunks
    all_chunks = []
    for doc_path, content in documents:
        rel_path = doc_path.relative_to(topic_dir)
        chunks = parse_markdown_sections(content, str(rel_path))
        all_chunks.extend(chunks)
    
    print(f"Parsed into {len(all_chunks)} chunks")
    
    # Create embeddings
    print("Creating OpenAI embeddings...")
    chunk_texts = [f"{c.section}\n\n{c.content}" for c in all_chunks]
    embeddings, total_tokens = embed_batch(client, chunk_texts)
    
    # Estimate cost
    embed_cost = (total_tokens / 1000) * PRICING["text-embedding-3-large"]["input"]
    print(f"Embedding cost: ${embed_cost:.4f} ({total_tokens:,} tokens)")
    
    # Build index
    index = {
        'chunks': [
            {
                'id': c.id,
                'content': c.content,
                'source': c.source_file,
                'section': c.section,
                'metadata': c.metadata
            }
            for c in all_chunks
        ],
        'embeddings': embeddings,
        'model': EMBEDDING_MODEL,
        'dimensions': EMBEDDING_DIMENSIONS,
        'version': '2.0-gpt52',
        'topic': topic,
        'build_tokens': total_tokens,
    }
    
    # Save
    with open(index_file, 'wb') as f:
        pickle.dump(index, f)
    
    print(f"✅ Index saved to {index_file}")
    print(f"   Chunks: {len(all_chunks)}")
    print(f"   Size: {index_file.stat().st_size / 1024 / 1024:.2f} MB")
    return index

# ============================================================================
# RAG QUERY
# ============================================================================
def query_rag(client: "OpenAI", index: Dict, query: str, top_k: int = 10) -> Tuple[List[Dict], int]:
    """Query the RAG index and return top-k relevant chunks."""
    
    query_embedding, tokens = embed_text(client, query)
    
    # Compute similarities
    similarities = []
    for i, emb in enumerate(index['embeddings']):
        sim = cosine_similarity(query_embedding, emb)
        similarities.append((i, sim))
    
    # Sort by similarity
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Return top-k
    results = []
    for idx, score in similarities[:top_k]:
        chunk = index['chunks'][idx]
        results.append({
            'score': score,
            'content': chunk['content'],
            'source': chunk['source'],
            'section': chunk['section'],
        })
    
    return results, tokens

# ============================================================================
# ANALYSIS PROMPTS V2
# ============================================================================
ANALYSIS_PROMPTS = {
    'contradictions': """You are a physics document analyst with expertise in mathematical physics and Yang-Mills theory.

### Task
Analyze the following synthesis document for internal contradictions.

### Instructions
1. Read the entire document carefully, chapter by chapter
2. For each claim, check if any other chapter makes a conflicting claim
3. For each contradiction found, provide:
   - Chapter A: [section reference]
   - Claim A: [exact quote or paraphrase]
   - Chapter B: [section reference]  
   - Claim B: [exact quote or paraphrase]
   - Nature of contradiction: [explain why these conflict]
   - Severity: [CRITICAL/MAJOR/MINOR]

4. Focus especially on:
   - Mathematical constants (ρ, σ, λ, etc.) with conflicting definitions
   - Claims about what is "proven" vs "conjectured"
   - Scale dependence claims (a→0 behavior)
   - Polarity claims for different strata (reducibles vs Gribov horizon)
   - Riccati equilibrium values

5. At the END, provide a summary count:
   - CRITICAL: X
   - MAJOR: X
   - MINOR: X

Return a structured analysis with ALL contradictions found.""",

    'gaps': """You are a mathematical physicist reviewing a proof synthesis.

### Task
Identify logical gaps in the argument chain.

### Instructions
1. Trace the logical flow from the abstract through to the conclusions
2. For each step that assumes an unproven claim, document:
   - Location: [chapter.section]
   - Claim being assumed: [description]
   - What would be needed to prove it: [description]
   - Status: [FRONTIER/OPEN/MISSING/BROKEN]

3. Create a dependency chain showing:
   - Which results depend on which earlier results
   - Where the chain breaks (unproven assumptions)

4. Focus on:
   - Steps from lattice to continuum
   - Steps from spectral gap to mass gap
   - Uniform bound claims
   - Countable union/covering arguments

5. At the END, count issues by status:
   - BROKEN: X (logical flaws)
   - MISSING: X (no argument given)
   - OPEN: X (acknowledged conjecture)
   - FRONTIER: X (plausible but unproven)

Return a complete gap analysis with dependency information.""",

    'redundancy': """You are a technical editor optimizing a physics document.

### Task
Identify redundant content that could be consolidated.

### Instructions
1. For each chapter, extract the key mathematical concepts covered
2. Find chapters with significant concept overlap (same equations, same theorems)
3. Recommend specific consolidations in order of impact

4. Check for:
   - Same theorem stated multiple times
   - Same equation derived in different chapters
   - Overlapping explanations of same concept
   - Especially: Schur complement, Riccati equation, Horizontal gradient lemma

5. For each redundancy:
   - Chapters involved
   - Overlap type (duplicate proof, restated theorem, repeated narrative)
   - Recommended action (merge A→B, delete C, add cross-reference)
   
6. At the END, estimate:
   - Total redundant chapters: X
   - Potential line reduction: X%

Return a redundancy report with prioritized consolidation recommendations.""",

    'critical-path': """You are a proof strategist analyzing a mathematical physics document.

### Task
Identify the MINIMUM set of missing lemmas whose proof would complete the main argument.

### Instructions
1. First, identify the document's main claim (the "theorem" being proven)
2. Trace backward: what does this claim depend on?
3. For each dependency, determine if it is:
   - PROVEN (has rigorous proof or Lean verification)
   - USABLE (standard result, can cite)
   - MISSING (needs to be proven)

4. Build a dependency tree and find the MINIMAL SET of missing pieces

5. For each item on the critical path:
   - Name/description
   - Why it's essential (what breaks without it)
   - Difficulty estimate (1-10)
   - Suggested approach

6. OUTPUT FORMAT:
   ## Critical Path (X items)
   1. [Most blocking item first]
   2. ...
   
   ## Dependency Tree
   [ASCII or markdown tree]
   
   ## Recommended Attack Order
   [Start with easiest items that unblock the most]

This is a strategic analysis, not an exhaustive audit.""",

    'fixes': """You are a physics editor proposing concrete fixes for a document.

### Task
Given the document with [BROKEN], [OPEN], [FRONTIER] markers, propose specific fixes.

### Instructions
1. Find all sections marked with status tags
2. For each [BROKEN] section:
   - Quote the problematic claim
   - Explain why it's broken
   - Propose 1-3 specific alternatives that would fix it
   
3. For each [OPEN] section:
   - Explain what would need to be proven
   - Suggest references or approaches
   
4. For CRITICAL severity issues:
   - Provide exact replacement text (markdown)

5. OUTPUT FORMAT:
   ## Fixes Required (X items)
   
   ### Fix 1: [Section]
   **Problem:** ...
   **Proposed Fix:**
   ```markdown
   [exact replacement text]
   ```
   
Return actionable fixes, not just descriptions.""",

    'full': """You are a senior physics reviewer performing a comprehensive quality analysis.

### Task
Perform a complete quality analysis of this physics synthesis document.

### Analysis Required
1. **CONTRADICTIONS**: Find claims that conflict with each other
2. **GAPS**: Find logical steps that assume unproven claims
3. **REDUNDANCY**: Find chapters covering the same content
4. **CONSISTENCY**: Check mathematical notation consistency
5. **COMPLETENESS**: Does the document achieve its stated goals?

For each issue found, provide:
- Location (chapter/section)
- Description of issue
- Severity (CRITICAL/MAJOR/MINOR)
- Recommended fix

### Summary Format (at end)
| Category | CRITICAL | MAJOR | MINOR |
|----------|----------|-------|-------|
| Contradictions | X | X | X |
| Gaps | X | X | X |
| Redundancy | X | X | X |

Be thorough but fair. Acknowledge what is done well.""",
}

# ============================================================================
# GPT-5.2 ANALYSIS FUNCTIONS
# ============================================================================
def analyze_document_with_gpt52(
    client: "OpenAI",
    document: str,
    analysis_type: str,
    index: Optional[Dict] = None
) -> AnalysisResult:
    """
    Use GPT-5.2 to analyze a physics synthesis document.
    
    analysis_type: 'contradictions' | 'gaps' | 'redundancy' | 'critical-path' | 'fixes' | 'full'
    """
    
    system_prompt = ANALYSIS_PROMPTS.get(analysis_type, ANALYSIS_PROMPTS['full'])
    
    user_message = f"""### Document to Analyze

{document}

### Analysis Required: {analysis_type.upper()}

Provide your complete analysis now."""

    # Call GPT-5.2
    print(f"Calling GPT-5.2 for {analysis_type} analysis...")
    start_time = datetime.now()
    
    response = client.chat.completions.create(
        model=GPT52_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.1,  # Low for consistency
        max_completion_tokens=MAX_OUTPUT_TOKENS
    )
    
    elapsed = (datetime.now() - start_time).total_seconds()
    
    raw_response = response.choices[0].message.content
    
    # Track usage
    usage = TokenUsage(
        input_tokens=response.usage.prompt_tokens,
        output_tokens=response.usage.completion_tokens,
    )
    
    # Parse severity counts from response
    severity_counts = parse_severity_counts(raw_response)
    
    print(f"Analysis complete in {elapsed:.1f}s")
    print(f"Tokens: {usage.input_tokens:,} in / {usage.output_tokens:,} out")
    print(f"Estimated cost: ${usage.estimated_cost:.4f}")
    if severity_counts:
        print(f"Severities: {severity_counts}")
    
    return AnalysisResult(
        analysis_type=analysis_type,
        document=document[:100] + "...",
        raw_response=raw_response,
        usage=usage,
        severity_counts=severity_counts
    )

def parse_severity_counts(text: str) -> Dict[str, int]:
    """Extract severity counts from analysis response."""
    counts = {}
    
    # Look for patterns like "CRITICAL: 3" or "- CRITICAL: 3"
    for severity in ['CRITICAL', 'MAJOR', 'MINOR', 'BROKEN', 'OPEN', 'FRONTIER', 'MISSING']:
        pattern = rf'{severity}[:\s]+(\d+)'
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            counts[severity] = int(matches[-1])  # Take last occurrence (usually the summary)
    
    return counts

def extract_claims_from_analysis(analysis_text: str) -> List[str]:
    """Extract verifiable claims from GPT-5.2 analysis output."""
    claims = []
    
    # Look for Claim A/Claim B patterns in contradiction reports
    claim_patterns = [
        r'\*\*Claim [AB]:\*\*\s*["""](.*?)["""]',  # **Claim A:** "text"
        r'- Claim [AB]:\s*["""](.*?)["""]',  # - Claim A: "text"
        r'\*\*Claim [AB]:\*\*\s*([^*\n]+)',  # **Claim A:** text without quotes
        r'Claim:\s*["""](.*?)["""]',  # Claim: "text"
    ]
    
    for pattern in claim_patterns:
        found = re.findall(pattern, analysis_text, re.IGNORECASE | re.DOTALL)
        claims.extend([c.strip() for c in found if len(c.strip()) > 20])
    
    # Deduplicate while preserving order
    seen = set()
    unique_claims = []
    for claim in claims:
        claim_key = claim[:100].lower()  # Use first 100 chars for dedup
        if claim_key not in seen:
            seen.add(claim_key)
            unique_claims.append(claim)
    
    return unique_claims[:10]  # Limit to 10 most important claims

def auto_verify_claims(claims: List[str], client: "OpenAI", index: Dict) -> Dict[str, Any]:
    """Automatically verify extracted claims using local models with RAG context."""
    if not HAS_OLLAMA or not check_ollama_available():
        return {"error": "Ollama not available", "verified": 0}
    
    results = []
    
    print(f"\n🔬 AUTO-VERIFYING {len(claims)} claims with local models...")
    print("=" * 70)
    
    for i, claim in enumerate(claims):
        print(f"\n[{i+1}/{len(claims)}] Verifying: {claim[:80]}...")
        
        # Get RAG context for this claim
        rag_context = None
        if client and index:
            try:
                rag_results, _ = query_rag(client, index, claim, top_k=3)
                rag_context = "\n\n".join([
                    f"Source: {r['source']} - {r['section']}\n{r['content'][:400]}"
                    for r in rag_results
                ])
            except Exception as e:
                print(f"   RAG error: {e}")
        
        # Run local verification (using fastest model for efficiency)
        result = local_verify_math(claim, model="phi4-mini", rag_context=rag_context)
        
        verdict = result.get("verdict", "ERROR")
        results.append({
            "claim": claim[:200],
            "verdict": verdict,
            "model": "phi4-mini",
            "has_context": rag_context is not None
        })
        
        # Print result
        icon = "✅" if verdict == "TRUE" else "❌" if verdict == "FALSE" else "❓"
        print(f"   {icon} Verdict: {verdict}")
    
    # Summary
    true_count = sum(1 for r in results if r["verdict"] == "TRUE")
    false_count = sum(1 for r in results if r["verdict"] == "FALSE")
    unclear_count = sum(1 for r in results if r["verdict"] == "UNCLEAR")
    
    print(f"\n📊 VERIFICATION SUMMARY:")
    print(f"   ✅ TRUE: {true_count}  ❌ FALSE: {false_count}  ❓ UNCLEAR: {unclear_count}")
    
    return {
        "verified": len(results),
        "true": true_count,
        "false": false_count,
        "unclear": unclear_count,
        "details": results
    }

# ============================================================================
# REPORT GENERATION
# ============================================================================
def generate_report(result: AnalysisResult, output_path: Path, verification_results: Optional[Dict] = None):
    """Generate a markdown report from analysis results."""
    
    # Build severity summary
    severity_table = ""
    if result.severity_counts:
        severity_table = "\n## Severity Summary\n\n| Level | Count |\n|-------|-------|\n"
        for level, count in result.severity_counts.items():
            severity_table += f"| {level} | {count} |\n"
        severity_table += "\n"
    
    # Build verification section if available
    verification_section = ""
    if verification_results and verification_results.get('verified', 0) > 0:
        v = verification_results
        verification_section = f"""
## Local Model Verification

| Result | Count |
|--------|-------|
| ✅ TRUE | {v.get('true', 0)} |
| ❌ FALSE | {v.get('false', 0)} |
| ❓ UNCLEAR | {v.get('unclear', 0)} |

"""
    
    report = f"""# GPT-5.2 Physics Document Analysis Report

**Analysis Type:** {result.analysis_type.upper()}
**Generated:** {result.timestamp}
**Model:** {GPT52_MODEL}

## Cost & Usage

| Metric | Value |
|--------|-------|
| Input Tokens | {result.usage.input_tokens:,} |
| Output Tokens | {result.usage.output_tokens:,} |
| Estimated Cost | ${result.usage.estimated_cost:.4f} |
{severity_table}
---

## Analysis Results

{result.raw_response}

---

*Report generated by GPT-5.2 Physics RAG Analyzer v2.0*
"""
    
    output_path.write_text(report)
    print(f"Report saved to: {output_path}")

# ============================================================================
# MAIN FUNCTIONS
# ============================================================================
def cmd_build_index(args):
    """Build the OpenAI embedding index."""
    if hasattr(args, 'topic') and args.topic:
        # Build index for specific topic
        build_topic_index(args.topic, force_rebuild=args.force)
    elif hasattr(args, 'all') and args.all:
        # Build indices for all topics
        print(f"Building GPT-5.2 indices for all {len(SUBJECT_FOLDERS)} subject folders...")
        for topic in SUBJECT_FOLDERS:
            print(f"\n{'='*60}")
            build_topic_index(topic, force_rebuild=args.force)
        print(f"\n{'='*60}")
        print("All indices built.")
    else:
        # Build central index (legacy)
        build_openai_index(force_rebuild=args.force)
    print("Index build complete.")

def cmd_analyze(args):
    """Run analysis on a synthesis document."""
    client = get_openai_client()
    if not client:
        print("ERROR: OpenAI client not available")
        return
    
    # Determine paths based on --topic or direct document
    output_dir = ANALYSIS_OUTPUT_DIR  # default
    rag_index_path = None
    
    if hasattr(args, 'topic') and args.topic:
        # Topic mode: analyze any subject folder
        try:
            doc_path, rag_index_path, output_dir = resolve_topic_paths(args.topic)
            print(f"Topic: {args.topic}")
            if rag_index_path:
                print(f"Using existing RAG index: {rag_index_path.name}")
        except FileNotFoundError as e:
            print(f"ERROR: {e}")
            return
    else:
        # Direct document mode (legacy)
        doc_path = SYNTHESIS_DIR / args.document
        if not doc_path.exists():
            doc_path = SYNTHESIS_DIR / (args.document + ".md")
        if not doc_path.exists():
            print(f"ERROR: Document not found: {doc_path}")
            return
    
    document = doc_path.read_text()
    print(f"Loaded document: {doc_path.name} ({len(document):,} chars)")
    
    # Load index for RAG support (use per-folder index if available, else central)
    if rag_index_path and rag_index_path.exists():
        print(f"Loading per-folder index...")
        with open(rag_index_path, 'rb') as f:
            index = pickle.load(f)
    else:
        index = build_openai_index()
    
    # Run GPT-5.2 analysis
    result = analyze_document_with_gpt52(
        client=client,
        document=document,
        analysis_type=args.type,
        index=index
    )
    
    # === AUTO-VERIFY WITH LOCAL MODELS ===
    verification_results = None
    if not getattr(args, 'skip_verify', False):
        # Extract claims from GPT-5.2 output
        claims = extract_claims_from_analysis(result.raw_response)
        
        if claims:
            # Run automatic local verification
            verification_results = auto_verify_claims(claims, client, index)
    
    # Generate report (include verification results)
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    doc_name = doc_path.stem  # Use actual document name
    report_path = output_dir / f"{args.type}_{doc_name}_{timestamp}.md"
    
    generate_report(result, report_path, verification_results)
    
    # Also print to console
    print("\n" + "="*70)
    print(f" ANALYSIS COMPLETE: {args.type.upper()}")
    print("="*70)
    print(result.raw_response[:2000])
    if len(result.raw_response) > 2000:
        print(f"\n... [truncated, see full report at {report_path}]")

def cmd_analyze_all(args):
    """Run analysis on all synthesis documents."""
    client = get_openai_client()
    if not client:
        print("ERROR: OpenAI client not available")
        return
    
    # Find all synthesis documents
    synthesis_docs = list(SYNTHESIS_DIR.glob("Synthesis_*.md"))
    print(f"Found {len(synthesis_docs)} synthesis documents")
    
    total_usage = TokenUsage()
    
    for doc_path in sorted(synthesis_docs):
        print(f"\n{'='*70}")
        print(f"Analyzing: {doc_path.name}")
        print("="*70)
        
        document = doc_path.read_text()
        index = build_openai_index()
        
        result = analyze_document_with_gpt52(
            client=client,
            document=document,
            analysis_type=args.type,
            index=index
        )
        
        # Accumulate usage
        total_usage.input_tokens += result.usage.input_tokens
        total_usage.output_tokens += result.usage.output_tokens
        
        # Save report
        ANALYSIS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        doc_name = doc_path.stem
        report_path = ANALYSIS_OUTPUT_DIR / f"{args.type}_{doc_name}_{timestamp}.md"
        generate_report(result, report_path)
    
    print(f"\n{'='*70}")
    print(f" ALL ANALYSES COMPLETE")
    print("="*70)
    print(f"Total tokens: {total_usage.total_tokens:,}")
    print(f"Total estimated cost: ${total_usage.estimated_cost:.4f}")

def cmd_query(args):
    """Query the RAG index."""
    client = get_openai_client()
    if not client:
        print("ERROR: OpenAI client not available")
        return
    
    index = build_openai_index()
    
    results, tokens = query_rag(client, index, args.query, top_k=args.top)
    
    print(f"\nQuery: '{args.query}' ({tokens} tokens)")
    print("="*70)
    
    for i, r in enumerate(results, 1):
        print(f"\n[{i}] Score: {r['score']:.4f}")
        print(f"    Source: {r['source']}")
        print(f"    Section: {r['section']}")
        print("-"*60)
        print(r['content'][:500])

# ============================================================================
# LOCAL MODEL COMMAND HANDLERS
# ============================================================================
def cmd_screen(args):
    """Quick local screening of a document."""
    if not check_ollama_available():
        print("ERROR: Ollama not available. Start Ollama with: ollama serve")
        return
    
    # Load document
    doc_path = SYNTHESIS_DIR / args.document
    if not doc_path.exists():
        doc_path = SYNTHESIS_DIR / (args.document + ".md")
    if not doc_path.exists():
        print(f"ERROR: Document not found: {doc_path}")
        return
    
    document = doc_path.read_text()
    print(f"Screening: {doc_path.name} ({len(document):,} chars)")
    print(f"Model: {args.model} (FREE)")
    print("-" * 70)
    
    result = local_screen_equations(document, model=args.model)
    
    if result.get("status") == "success":
        print("\n📋 Extracted Equations:\n")
        print(result["response"])
    else:
        print(f"ERROR: {result.get('error')}")

def cmd_verify_math(args):
    """Verify a mathematical claim using local model with RAG context."""
    if not check_ollama_available():
        print("ERROR: Ollama not available")
        return
    
    # Get OpenAI client for RAG embedding
    client = get_openai_client()
    if not client:
        print("WARNING: OpenAI client not available - running without RAG context")
        rag_context = None
    else:
        # Load RAG index
        index = build_openai_index()
        if not index:
            print("WARNING: RAG index not available - running without context")
            rag_context = None
        else:
            # Query for relevant context
            print(f"🔍 Retrieving relevant source material...")
            results, tokens = query_rag(client, index, args.claim, top_k=5)
            
            # Build context string
            rag_context = "\n\n---\n\n".join([
                f"**Source:** {r['source']} - {r['section']}\n{r['content'][:800]}"
                for r in results
            ])
            print(f"   Retrieved {len(results)} chunks ({tokens} embedding tokens)")
    
    print(f"\nVerifying: {args.claim}")
    print(f"Model: {args.model} (FREE)")
    print(f"RAG Context: {'YES' if rag_context else 'NO'}")
    print("-" * 70)
    
    result = local_verify_math(args.claim, model=args.model, rag_context=rag_context)
    
    if result.get("status") == "success":
        print(f"\n🎯 Verdict: {result['verdict']}")
        print(f"\n📝 Reasoning:\n{result['reasoning']}")
    else:
        print(f"ERROR: {result.get('error')}")

def cmd_ensemble_check(args):
    """Check a claim with multiple local models using RAG context."""
    if not check_ollama_available():
        print("ERROR: Ollama not available")
        return
    
    # Get OpenAI client for RAG embedding
    client = get_openai_client()
    if not client:
        print("WARNING: OpenAI client not available - running without RAG context")
        rag_context = None
    else:
        # Load RAG index
        index = build_openai_index()
        if not index:
            print("WARNING: RAG index not available - running without context")
            rag_context = None
        else:
            # Query for relevant context
            print(f"🔍 Retrieving relevant source material...")
            results, tokens = query_rag(client, index, args.claim, top_k=5)
            
            # Build context string
            rag_context = "\n\n---\n\n".join([
                f"**Source:** {r['source']} - {r['section']}\n{r['content'][:600]}"
                for r in results
            ])
            print(f"   Retrieved {len(results)} chunks ({tokens} embedding tokens)")
    
    print(f"\nEnsemble checking: {args.claim}")
    print("Models: phi4-mini, qwen2-math:7b, deepseek-r1:14b (ALL FREE)")
    print(f"RAG Context: {'YES' if rag_context else 'NO'}")
    print("-" * 70)
    
    result = ensemble_check(args.claim, rag_context=rag_context)
    
    print(f"\n🎯 Consensus: {'YES' if result.get('consensus') else 'NO - DISAGREEMENT'}")
    print(f"📊 Final Verdict: {result.get('verdict')}")
    
    if result.get('requires_human'):
        print("\n⚠️  REQUIRES HUMAN REVIEW - Models disagree!")
    
    print("\n📝 Individual Results:")
    for model, data in result.get('results', {}).items():
        print(f"\n  [{model}]")
        if 'error' in data:
            print(f"    Error: {data['error']}")
        else:
            print(f"    Verdict: {data.get('verdict')}")
            print(f"    Reasoning: {data.get('reasoning', '')[:200]}...")

def cmd_deep_reason(args):
    """Deep chain-of-thought reasoning with DeepSeek-R1."""
    if not check_ollama_available():
        print("ERROR: Ollama not available")
        return
    
    print(f"Question: {args.question}")
    print("Model: deepseek-r1:14b (FREE, ~30s)")
    print("-" * 70)
    
    result = local_deep_reasoning(args.question)
    
    if result.get("status") == "success":
        print(f"\n{result['response']}")
    else:
        print(f"ERROR: {result.get('error')}")

def cmd_models(args):
    """List available models."""
    print("=" * 70)
    print(" AVAILABLE MODELS")
    print("=" * 70)
    
    print("\n📦 LOCAL MODELS (FREE, via Ollama):")
    if HAS_OLLAMA:
        try:
            response = ollama.list()
            # Handle both dict and object response formats
            if hasattr(response, 'models'):
                models_list = response.models
            else:
                models_list = response.get('models', [])
            
            for m in models_list:
                if hasattr(m, 'model'):
                    name = m.model
                    size = m.size if hasattr(m, 'size') else 0
                else:
                    name = m.get('name', 'unknown')
                    size = m.get('size', 0)
                size_gb = size / (1024**3)
                print(f"  ✅ {name:30} ({size_gb:.1f} GB)")
        except Exception as e:
            print(f"  ❌ Ollama not running: {e}")
    else:
        print("  ❌ Ollama not installed. Run: pip install ollama")
    
    print("\n☁️  CLOUD MODELS (API, paid):")
    print(f"  • gpt-5.2         Deep analysis ($0.15/doc)")
    print(f"  • gpt-4o-mini     Quick screening ($0.01/doc)")
    
    print("\n📋 RECOMMENDED USAGE:")
    print("  1. screen         → phi4-mini (FREE, fast)")
    print("  2. verify-math    → qwen2-math:7b (FREE, math-specialized)")
    print("  3. ensemble-check → ALL 3 local models (FREE, disagreement detection)")
    print("  4. deep-reason    → deepseek-r1:14b (FREE, chain-of-thought)")
    print("  5. analyze        → gpt-5.2 (paid, only for deep analysis)")

# ============================================================================
# CLI
# ============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="GPT-5.2 Physics RAG Analyzer v2.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python gpt52_physics_analyzer.py build-index
  python gpt52_physics_analyzer.py analyze Synthesis_15_Polarity_Gribov.md --type contradictions
  python gpt52_physics_analyzer.py analyze Synthesis_15.md --type critical-path
  python gpt52_physics_analyzer.py analyze Synthesis_15.md --type fixes
  python gpt52_physics_analyzer.py analyze-all --type contradictions
  python gpt52_physics_analyzer.py query "Weyl curvature lower bound"
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # build-index command
    build_parser = subparsers.add_parser('build-index', help='Build OpenAI embedding index')
    build_parser.add_argument('--force', '-f', action='store_true', help='Force rebuild')
    build_parser.add_argument('--topic', '-T', help='Build index for specific topic (e.g., SCALING_LIMIT)')
    build_parser.add_argument('--all', '-a', action='store_true', help='Build indices for all subject folders')
    
    # analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze a synthesis document')
    analyze_parser.add_argument('document', nargs='?', default=None,
                                help='Document filename (e.g., Synthesis_15.md) - optional if --topic used')
    analyze_parser.add_argument('--topic', '-T',
                                help='Subject folder to analyze (e.g., SCALING_LIMIT, HAAR, RICCATI)')
    analyze_parser.add_argument('--type', '-t', 
                                choices=['contradictions', 'gaps', 'redundancy', 'critical-path', 'fixes', 'full'],
                                default='full',
                                help='Type of analysis')
    
    # analyze-all command
    analyze_all_parser = subparsers.add_parser('analyze-all', help='Analyze all synthesis documents')
    analyze_all_parser.add_argument('--type', '-t',
                                    choices=['contradictions', 'gaps', 'redundancy', 'critical-path', 'fixes', 'full'],
                                    default='contradictions',
                                    help='Type of analysis')
    
    # query command
    query_parser = subparsers.add_parser('query', help='Query the RAG index')
    query_parser.add_argument('query', help='Query string')
    query_parser.add_argument('--top', '-k', type=int, default=5, help='Number of results')
    
    # === NEW LOCAL MODEL COMMANDS ===
    
    # screen command (local, FREE)
    screen_parser = subparsers.add_parser('screen', help='Quick local screening (FREE, ~5s)')
    screen_parser.add_argument('document', help='Document filename')
    screen_parser.add_argument('--model', '-m', default='phi4-mini', help='Local model to use')
    
    # verify-math command (local, FREE)
    verify_parser = subparsers.add_parser('verify-math', help='Verify a math claim locally (FREE)')
    verify_parser.add_argument('claim', help='Mathematical claim to verify')
    verify_parser.add_argument('--model', '-m', default='qwen2-math:7b', help='Model to use')
    
    # ensemble-check command (local, FREE)
    ensemble_parser = subparsers.add_parser('ensemble-check', help='Check claim with multiple models (FREE)')
    ensemble_parser.add_argument('claim', help='Claim to verify across models')
    
    # deep-reason command (local, FREE)
    deep_parser = subparsers.add_parser('deep-reason', help='Deep reasoning with DeepSeek-R1 (FREE, ~30s)')
    deep_parser.add_argument('question', help='Question for chain-of-thought reasoning')
    
    # models command - show available models
    models_parser = subparsers.add_parser('models', help='List available local and cloud models')
    
    args = parser.parse_args()
    
    if args.command == 'build-index':
        cmd_build_index(args)
    elif args.command == 'analyze':
        cmd_analyze(args)
    elif args.command == 'analyze-all':
        cmd_analyze_all(args)
    elif args.command == 'query':
        cmd_query(args)
    elif args.command == 'screen':
        cmd_screen(args)
    elif args.command == 'verify-math':
        cmd_verify_math(args)
    elif args.command == 'ensemble-check':
        cmd_ensemble_check(args)
    elif args.command == 'deep-reason':
        cmd_deep_reason(args)
    elif args.command == 'models':
        cmd_models(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
