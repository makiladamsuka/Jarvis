import requests

try:
    url = "http://localhost:7860/api/v1/run/71a484ec-070e-4e59-bcae-f00583f43e98"
except KeyError:
    raise ValueError("APP_TOKEN environment variable not found. Please set your API key in the .env file.")

headers = {
    "Content-Type": "application/json"
}


def api(user_input):
    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": user_input
    }

    try:
        # Send API request
        response = requests.request("POST", url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes

        data = response.json()  # Parse JSON response

        # Access the message from the nested JSON data
        answer = data['outputs'][0]['outputs'][0]['outputs']['message']['message']
        return answer

    except requests.exceptions.RequestException as e:
        return e
    except ValueError as e:
        return e
    except KeyError as e:
        return e
