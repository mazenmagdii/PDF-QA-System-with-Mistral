from src.embedder import embed_text

def search_index(query, embed_model, vectorstore, chunks, k=5):
    query_embedding = embed_text(embed_model, query)
    distances, indices=vectorstore.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]