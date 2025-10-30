import json
import pandas as pd
import openpyxl
import os 
from pathlib import Path


#current_file=Path(__file__).resolve()
#target_file=current_file.parent / "test.json"
#print(target_file)

def Convert_JSON_to_EXCEL (json_filename='test.json'):
    #json_path = os.path.abspath('test.json')
    current_file_JSON=Path(__file__).resolve()
    target_file_JSON=current_file_JSON.parent / "test.json"
    current_file_EXCEL=Path(__file__).resolve()
    target_file_EXCEL=current_file_EXCEL.parent / "Exports.xlsx"
    #excel_path=os.path.abspath('Exports.xlsx')
    #Load JSON data
    with open(target_file_JSON) as file:
        data=json.load(file)


    # Convert json data to pandas dataframe
    df = pd.DataFrame([data], index=[0])
    print(df)
    #print(target_file)
    if os.path.exists(target_file_EXCEL):
        os.remove(target_file_EXCEL)
        df.to_excel('Exports.xlsx', index=False)
#convert_JSON_to_EXCEL()
    else:
        df.to_excel('Exports.xlsx', index=False)


#convert_JSON_to_EXCEL()

Convert_JSON_to_EXCEL()