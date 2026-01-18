# 📚 Optimized PDF-QA System with Quantized Mistral-Nemo

A high-performance RAG (Retrieval-Augmented Generation) system designed for low-latency document interrogation. This project features a **4-bit quantized Mistral-Nemo** model to achieve lightning-fast inference on T4 GPU, accessible via a custom Streamlit interface.



## 🚀 Technical Highlights

* **4-Bit Quantization (BitsAndBytes):** The model is loaded in 4-bit precision to significantly reduce VRAM usage while maintaining high accuracy, enabling parameter performance on consumer-grade hardware.
* **Hybrid Cloud-Local Architecture:** Leverages Kaggle’s T4 GPU for heavy computation (Backend) while providing a lightweight Streamlit interface for the user (Frontend).
* **Deterministic Retrieval:** Utilizes FAISS (Facebook AI Similarity Search) for sub-millisecond document chunk retrieval based on semantic similarity.


## 🏗️ System Architecture

The system operates through a secured bridge between the GPU environment and the local client:

1.  **Backend (Kaggle/FastAPI):** Orchestrates the document embedding pipeline, vector storage, and the quantized LLM execution using the Mistral-Nemo-Instruct-2407 model.
2.  **Tunneling (Ngrok):** Provides a secure, low-latency tunnel to expose the local FastAPI server to the public internet.
3.  **Frontend (Streamlit):** A responsive UI that handles PDF processing, stateful chat history, and real-time response rendering.

## 🛠️ Tech Stack

* **Model:** Mistral-Nemo-Instruct-2407 (4-bit Quantized)
* **Vector Engine:** FAISS
* **Embeddings:** `all-MiniLM-L6-v2` (Sentence-Transformers)
* **API Framework:** FastAPI
* **UI Framework:** Streamlit
* **PDF Engine:** PyMuPDF (fitz)

## 📋 Installation & Setup

### 1. The Brain (Backend)
1. Open the notebook `mistral_rag.ipynb` in Kaggle.
2. Ensure you are using the **T4 GPU** accelerator.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Input your `NGROK_TOKEN` and define a secure `API_KEY` in the configuration cell.
5. Run all cells. Copy the generated `.ngrok-free.dev` URL from the output.

### 2. The Interface (Frontend)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open **app.py** and paste the Ngrok URL into the BACKEND_URL variable while adding the endpoint `/generate` like in **app.py**.
3. Run the application from your terminal:
    ```bash
    streamlit run app.py
    ```
