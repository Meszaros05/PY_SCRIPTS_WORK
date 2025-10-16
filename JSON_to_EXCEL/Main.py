import json
import pandas as pd
import openpyxl
import os 



#Relative path to the file
relative_path = 'test.json'
# Convert to absolute path
absolute_path = os.path.abspath(relative_path)
#--------------------------------------------------------------


#Load JSON data
with open(absolute_path) as file:
    data=json.load(file)

print(data)

# Convert json data to pandas dataframe
df = pd.DataFrame([data], index=[0]) 
print(df)
