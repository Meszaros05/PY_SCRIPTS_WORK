import requests
import json
import os
from pathlib import Path
import re


#OUTPUT_FILE'S NAME SHOULD BE NAMED AS IT IS DOWNLOADED FROM BROWSER

def Download_JSON(api_url="https://your-claroty-instance/api/v1/assets", api_token="", output_file="claroty_data.json"):

    #api_url = "https://your-claroty-instance/api/v1/assets"
    #api_token = "your_api_token_here"
    """
    Downloads JSON data from the Claroty API and saves it to a file.

    Parameters:
        api_url (str): The API endpoint URL.
        api_token (str): The bearer token for authentication.
        output_file (str): The filename to save the JSON data.

    Returns:
        bool: True if successful, False otherwise.
    """

    #Delete existing .JSON file
    pattern = re.compile(r".*\.json$", re.IGNORECASE)
    main_folder_path=Path(__file__).resolve().parent
    json_files=[f for f in main_folder_path.iterdir() if pattern.match(f.name)]
    
    if json_files:
        for file in json_files:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Failed to delete {file}:{e}")

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


Download_JSON()