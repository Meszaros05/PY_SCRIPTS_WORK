import json
import pandas as pd
import openpyxl
import os 
from pathlib import Path
from API_Handler.API_Handler import main_API_Handler
import time


def Waiter():
    # Path to the target file
    download_dir = Path(r"C:\Users\a829052\Downloads")
    
    # Timeout in seconds
    timeout = 5
    start_time = time.time()
    
    while True:
        files=list(download_dir.glob("downloadsasd*.json"))
        
        if files:
            target_file_JSON = max(files, key=lambda f: f.stat().st_mtime)
            return target_file_JSON  # Return the file path when found

        if time.time() - start_time > timeout:
            return None  # Timeout, no file found

        time.sleep(1)


#current_file=Path(__file__).resolve()
#target_file=current_file.parent / "test.json"
#print(target_file)
def Convert_JSON_to_EXCEL ():
    #json_path = os.path.abspath('test.json')
    #current_file_JSON=Path(__file__).resolve()
    #target_file_JSON=current_file_JSON.parent / "test.json"
    
    #target_file_JSON = Path(r"C:\Users\a829052\Downloads\download.json") #this using the download folder
    download_dir = Path(r"C:\Users\a829052\Downloads")
    current_file_EXCEL=Path(__file__).resolve()
    target_file_EXCEL=current_file_EXCEL.parent / "Exports.xlsx"
    #excel_path=os.path.abspath('Exports.xlsx')

    
    # Find the latest file with a specific pattern (e.g., .json)
    
    target_file_JSON=Waiter()
    if target_file_JSON:
        target_file_JSON = max(download_dir.glob("downloadsasd*.json"), key=lambda f: f.stat().st_mtime)
        #Load JSON data
        with open(target_file_JSON) as file:
            data=json.load(file)
    
        record=data["objects"]
    
        # Convert json data to pandas dataframe
        df = pd.DataFrame([record])
        df=pd.json_normalize(record)

        #print(target_file)
        if os.path.exists(target_file_EXCEL):
            os.remove(target_file_EXCEL)
            df.to_excel('Exports.xlsx', index=False)
    #convert_JSON_to_EXCEL()
        else:
            df.to_excel('Exports.xlsx', index=False)
    
    else: print("JSON file is not created")
    


#convert_JSON_to_EXCEL()
