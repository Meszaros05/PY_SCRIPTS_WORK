import json
import pandas as pd
import openpyxl
import os 
from pathlib import Path


current_file=Path(__file__).resolve()
target_file=current_file.parent / "test.json"
print(target_file)

def convert_JSON_to_EXCEL (json_filename='test.json'):
    json_path = os.path.abspath('test.json')
    excel_path=os.path.abspath('Exports.xlsx')
    #Load JSON data
    with open(json_path) as file:
        data=json.load(file)


    # Convert json data to pandas dataframe
    df = pd.DataFrame([data], index=[0])
    print(df)
    print(json_path)
    if os.path.exists(excel_path):
        os.remove(excel_path)
        df.to_excel('Exports.xlsx', index=False)
#convert_JSON_to_EXCEL()
    else:
        df.to_excel('Exports.xlsx', index=False)


#convert_JSON_to_EXCEL()

