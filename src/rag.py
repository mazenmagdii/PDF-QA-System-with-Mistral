from src.retriever import search_index
from src.generator import generate_text

def rag(query, embedder, vectorstore, docs, tokenizer, llms):
    relevant = search_index(query, embedder, vectorstore, docs)
    context="\n\n".join(relevant)
    return generate_text(llms, tokenizer, context, query)