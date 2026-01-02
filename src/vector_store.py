import faiss

def create_faiss_index(embeddings):
    dim=embeddings.shape[1]
    index=faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

