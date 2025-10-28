import requests
import json


api_url = "https://your-claroty-instance/api/v1/assets"
api_token = "your_api_token_here"


def download_json(api_url, api_token, output_file="claroty_data.json"):
    """
    Downloads JSON data from the Claroty API and saves it to a file.

    Parameters:
        api_url (str): The API endpoint URL.
        api_token (str): The bearer token for authentication.
        output_file (str): The filename to save the JSON data.

    Returns:
        bool: True if successful, False otherwise.
    """
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)

        print(f"✅ JSON data saved to {output_file}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to fetch data: {e}")
        return False
