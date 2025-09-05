# Chatbot with OpenRouter (Langflow)

This project demonstrates how to build and interact with a chatbot using
**Langflow** both locally and the **OpenRouter API**.

'app' folder contains a simple web app to interact with the chatbot.


## 📂 Project Structure

-   `app` → folder contains the web app code.
-   `api.py` → Python script to send chat requests.
-   `Chatbot flow with Openrouter.json` → Langflow flow definition
    (import this into Langflow).
-   `.env` → Stores API token (not uploaded to GitHub).
-   `requirements.txt` → Dependencies.
-   `README.md` → Project documentation.

------------------------------------------------------------------------

## 🚀 Setup Instructions

### 1. Install Langflow Locally

Follow the official installation guide:\
[Langflow Docs](https://docs.langflow.org/getting-started/)

For example, you can install using pip:

``` bash
pip install langflow
```

Run Langflow locally:

``` bash
langflow run
```

This usually starts a local server at:\
`http://localhost:7860`

------------------------------------------------------------------------

### 2. Import the Chatbot Flow

1.  Open your Langflow UI in the browser (`http://localhost:7860`).\
2.  Import the provided file **`Chatbot flow with Openrouter.json`**.\
3.  This sets up the chatbot pipeline (input → OpenRouter → output).

------------------------------------------------------------------------

### 3. Get an OpenRouter API Token

1.  Go to [OpenRouter](https://openrouter.ai/).\
2.  Sign up / log in.\
3.  Generate an API token from your account dashboard.

------------------------------------------------------------------------

### 4. Create a `.env` File

In your project root, create a file named `.env` with this content:

``` env
APP_TOKEN=your_openrouter_api_token_here
```


------------------------------------------------------------------------

### 5. Install Dependencies

Create a virtual environment and install required packages:

``` bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` should contain:

``` txt
requests
python-dotenv
```

------------------------------------------------------------------------

### 6. Run the API Script

Start your chatbot by running:

``` bash
python api.py
```

This will send a request to your locally running Langflow server using
OpenRouter as the model backend.


