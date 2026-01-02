from sentence_transformers import SentenceTransformer

def load_embedder():
    model_name_="sentence-transformers/all-MiniLM-L6-v2"
    return SentenceTransformer(model_name_)

def embed_text(model, texts):
    return model.encode(texts, show_progress_bar=False)