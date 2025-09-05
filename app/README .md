
# Jarvis: Web app with Langflow,Ollama Mistral & Streamlit

This repository contains a simple **Streamlit** frontend that acts like **Jarvis**, your personal AI assistant.  
It connects to a **Langflow AI** backend running locally and uses **Ollama** with the **Mistral** model to process user queries and return responses.

---

## Features

- **Jarvis-like AI Assistant**: Talk to the AI like you're chatting with Jarvis.  
- **Streamlit Frontend**: Easy-to-use web interface for interactions.  
- **Local Execution**: Runs fully on your machine using **Ollama** and **Langflow**.  
- **Mistral Model**: Powered by the **Mistral** LLM via **Ollama**.  

---

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)  
- [Ollama](https://ollama.com/) installed locally
- [Mistral model](https://ollama.com/library/mistral) for Ollama
- [Langflow](https://github.com/logspace-ai/langflow) running locally with API enabled  

---

## How It Works

1. **Streamlit** serves as the frontend (Jarvis UI).  
2. User input is sent to **Langflow** API running locally.  
3. Langflow uses **Ollama (Mistral)** to process the request.  
4. The AI (Jarvis) sends back the response to the frontend.  

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Ollama with Mistral**
   ```bash
   ollama run mistral
   ```

4. **Start Langflow**
   ```bash
   langflow run
   ```
5. **Import the Flow**  
   Import the provided Langflow flow file (`langflow_flow.json`) into your Langflow instance to set up the necessary flow for handling requests.

6. **Update API Endpoint**  
   In your Python script, set the correct Langflow API endpoint:
   ```python
   url = "http://localhost:7860/api/v1/run/<your-flow-id>"
   ```

---

## Usage

Launch the Streamlit frontend:
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` to interact with Jarvis.

---


