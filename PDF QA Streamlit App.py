import streamlit as st
import requests
import json
import time

# --- CONFIG ---
BACKEND_URL = "https://ungoaded-subdorsally-bethanie.ngrok-free.dev/generate"
API_KEY = "secret123"

st.set_page_config(page_title="AI PDF Chat", layout="wide")
st.title("📚 Chat with PDF")

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("Controls")
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
    
    st.divider()
    
    # THE 1st BLOCK: Clear Chat Button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.success("History cleared!")
        time.sleep(1) # Brief pause so the user sees the success message
        st.rerun()

# --- CHAT LOGIC ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask a question about the PDF..."):
    if not uploaded_file:
        st.error("Please upload a PDF in the sidebar first!")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Prepare Multi-part form data
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
        
        # We only send the last few messages to the backend to keep it fast
        # (The backend also handles trimming, but sending less data is better)
        history_data = json.dumps(st.session_state.messages[-5:]) 
        
        data = {
            "prompt": prompt,
            "history": history_data
        }
        headers = {"Authorization": f"Bearer {API_KEY}"}

        with st.chat_message("assistant"):
            start_time = time.time() # Start the timer
            with st.spinner("Analyzing context..."):
                try:
                    res = requests.post(BACKEND_URL, headers=headers, data=data, files=files, verify=False)
                    
                    if res.status_code == 200:
                        answer = res.json().get("response")
                        end_time = time.time() # End the timer
                        
                        # Show time taken
                        st.caption(f"⏱️ Response time: {round(end_time - start_time, 2)} seconds")
                        st.write(answer)
                        
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                    else:
                        st.error(f"Backend Error: {res.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")