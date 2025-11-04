import requests
import pandas as pd
import urllib3
from datetime import datetime
from pathlib import Path
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Constants
SERVER = "clarotyemc.nhy.hydro.com"
USER = "API_admin"
PASSWORD = "Admin123!"
VERIFY_SSL = False

def get_token():
    response = requests.post(
        f"https://{SERVER}/auth/authenticate",
        json={"username": USER, "password": PASSWORD},
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"},
        verify=VERIFY_SSL

    )
    
    data = response.json()
    return data.get("token")  #==> need to be called

def fetch_sites(token):
    response=requests.get(
        f"https://{SERVER}/ranger/sites",
        headers={
            "Authorization": token,
            "Accept":"Application/json"
            },
        params={"page": 1, "per_page": 100},
        verify=VERIFY_SSL,
        
    )
    download_path=Path(r"C:\Users\a829052\Downloads")
    filename=f"downloadsasd.json"
    filepath=download_path/filename

    with open(filepath,"w",encoding="utf-8") as f:
        f.write(response.text)
    response.raise_for_status()
    return response.json()




def main_API_Handler():
    token = get_token()
    print(token)
    fetch_sites(token)
    
    

if __name__ == "__main__":
    main_API_Handler()
