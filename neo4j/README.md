# Synapse Neo4j Vector Engine

A sophisticated vector embedding system using BGE-M3 transformers for semantic search and knowledge retrieval.

## Overview

This system provides semantic embeddings for text content using the state-of-the-art BGE-M3 model from BAAI. It stores embeddings in SQLite with Neo4j integration for knowledge graph operations.

## Features

- **BGE-M3 Embeddings**: Uses BAAI/bge-m3 transformer model for high-quality 1024-dimensional vectors
- **Local Processing**: No API keys required - runs completely on your machine
- **Fallback System**: Gracefully falls back to TF-IDF if transformer model unavailable
- **Hybrid Storage**: SQLite for vectors + Neo4j for knowledge graph
- **Similarity Search**: Cosine similarity search with configurable thresholds

## Quick Start

### Prerequisites

```bash
# Install dependencies
uv pip install -r requirements.txt
```

### Configuration

Set your embedding model in `.env`:

```bash
# Use BGE-M3 (recommended)
EMBEDDING_MODEL=BAAI/bge-m3

# Or fallback to simple TF-IDF
EMBEDDING_MODEL=simple_tfidf
```

### Basic Usage

```python
from vector_engine import VectorEngine

# Initialize engine
engine = VectorEngine()
engine.initialize_vector_store()

# Generate embeddings
text = "Your content here"
embedding = engine.generate_embedding(text)

# Store embedding
engine.store_embedding(node_id, file_path, content_hash, embedding)

# Search similar content
query_embedding = engine.generate_embedding("search query")
results = engine.similarity_search(query_embedding, top_k=5)
```

### CLI Testing

```bash
# Test embedding generation
python vector_engine.py "test text here"

# View statistics
python vector_engine.py --stats
```

## BGE-M3 Model Details

### What is BGE-M3?

BGE-M3 (Beijing Academy of Artificial Intelligence - Multilingual, Multifunctionality, Multimodality) is a cutting-edge embedding model that:

- **Multilingual**: Supports 100+ languages
- **High Quality**: State-of-the-art semantic understanding
- **1024 Dimensions**: Rich vector representations
- **Local Execution**: No external API dependencies

### Model Loading

The model is automatically downloaded from Hugging Face on first use:

```
Loading BGE-M3 model: BAAI/bge-m3
BGE-M3 model loaded successfully.
```

**Storage Location**: `~/.cache/huggingface/hub/`

**Download Size**: ~2.3GB (one-time download)

## Architecture

### Vector Storage Schema

**vector_metadata table:**
- `neo4j_node_id`: Link to Neo4j nodes
- `file_path`: Source file path
- `content_hash`: Content integrity verification
- `embedding_model`: Model used (e.g., "BAAI/bge-m3")
- `embedding_dim`: Vector dimensions (1024 for BGE-M3)

**vectors table:**
- `neo4j_node_id`: Node reference
- `vector_data`: Serialized numpy array
- `vector_norm`: Precomputed vector magnitude

### Similarity Search

Uses cosine similarity for semantic matching:

```python
similarity = dot_product / (query_norm * stored_norm)
```

## Error Handling

The system includes robust error handling:

1. **Model Loading Failures**: Falls back to TF-IDF
2. **Missing Dependencies**: Clear error messages with installation instructions
3. **Corrupted Embeddings**: Automatic regeneration
4. **Network Issues**: Offline operation after initial model download

## Performance

### BGE-M3 Performance
- **Quality**: Superior semantic understanding vs TF-IDF
- **Speed**: ~100ms per embedding (CPU)
- **Memory**: ~3GB RAM for model
- **Storage**: 8KB per 1024-dim vector

### TF-IDF Fallback
- **Quality**: Basic keyword matching
- **Speed**: ~1ms per embedding
- **Memory**: Minimal
- **Storage**: 3KB per 384-dim vector

## Integration

### With Ingestion Pipeline

```python
# In ingestion.py
embedding = vector_engine.generate_embedding(content, file_path)
vector_engine.store_embedding(node_id, file_path, content_hash, embedding)
```

### With Context Manager

```python
# In context_manager.py
query_embedding = vector_engine.generate_embedding(query)
similar_nodes = vector_engine.similarity_search(query_embedding)
```

## Troubleshooting

### Model Download Issues

```bash
# Check internet connection and retry
python vector_engine.py "test"
```

### Dependency Issues

```bash
# Reinstall dependencies
uv pip install --upgrade sentence-transformers numpy
```

### Storage Issues

```bash
# Clear and reinitialize
python -c "from vector_engine import VectorEngine; VectorEngine().clear_embeddings()"
```

## Development

### Testing New Models

To test different embedding models:

1. Update `EMBEDDING_MODEL` in `.env`
2. Modify `_initialize_transformer_model()` if needed
3. Clear existing embeddings: `engine.clear_embeddings()`
4. Re-run ingestion

### Custom Embedding Models

Extend the `VectorEngine` class:

```python
def custom_embedding(self, text: str) -> np.ndarray:
    # Your custom embedding logic
    return embedding_vector
```

## Files

- `vector_engine.py`: Main embedding engine
- `ingestion.py`: Content processing and embedding generation
- `context_manager.py`: Similarity search and retrieval
- `requirements.txt`: Python dependencies
- `.env`: Configuration (embedding model selection)

## License

Part of the Synapse System - see main project license.