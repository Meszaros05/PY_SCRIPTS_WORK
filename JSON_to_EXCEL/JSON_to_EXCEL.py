import json
import pandas as pd
import openpyxl
import os 




# Convert to absolute path
absolute_path = os.path.abspath('test.json')
#C:\Users\a829052\OneDrive - Norsk Hydro ASA\Dokumentumok\WORK\Python script\JSON_to_EXCEL\test.json

excel_path=os.path.abspath('Exports.xlsx')
#--------------------------------------------------------------


#Load JSON data
with open(absolute_path) as file:
    data=json.load(file)

print(data)

# Convert json data to pandas dataframe
df = pd.DataFrame([data], index=[0]) 
print(df)

df.to_excel('Exports.xlsx', index=False)



if os.path.exists(absolute_path):
    os.remove(excel_path)
    df.to_excel('Exports.xlsx', index=False)

else:
    df.to_excel('Exports.xlsx', index=False)
