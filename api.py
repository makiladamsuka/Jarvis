import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# API Configuration
try:
    api_key = os.environ["APP_TOKEN"]
except KeyError:
    raise ValueError("LANGFLOW_API_KEY environment variable not found. Please set your API key in the environment variables.")

url = "http://localhost:7860/api/v1/run/6ce59bf5-5dee-463b-96cf-bb1707e5583e"  # The complete API endpoint URL for this flow

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "What is the capital of France?"
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key  # Authentication key from environment variable
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes


    data = response.json()  # Parse JSON response

    answer = data['outputs'][0]['outputs'][0]['outputs']['message']['message']
    print(answer)
except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")