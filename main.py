import argparse
from src.pdf_loader import load_pdf
from src.chunker import chunk_text
from src.embedder import load_embedder, embed_text
from src.vector_store import create_faiss_index
from src.generator import load_llm
from src.rag import rag

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, required=True, help="Path to input PDF")
    parser.add_argument("--query", type=str, required=True, help="User question")
    args = parser.parse_args()

    # 1. Load user PDF
    text = load_pdf(args.pdf)

    # 2. Chunk text
    chunks = chunk_text(text)

    # 3. Embeddings
    embed_model = load_embedder()
    embeddings = embed_text(embed_model, chunks)

    # 4. Vector DB
    vs = create_faiss_index(embeddings)

    # 5. LLM
    tokenizer, llm = load_llm()

    # 6. RAG
    answer = rag(
        args.query,
        embed_model,
        vs,
        chunks,
        tokenizer,
        llm
    )

    print("\n=== RAG Answer ===")
    print(answer)
    print("==================")


if __name__ == "__main__":
    main()
