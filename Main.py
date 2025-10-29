import os
import sys

current_folder=os.path.abspath('Main.py')
parent_folder=os.path.dirname(current_folder)

#Add the module path to sys.path
JSON_dir=(os.path.join(parent_folder, 'JSON_to_EXCEL'))

sys.path.append(JSON_dir)

#from JSON_to_EXCEL import convert_JSON_to_EXCEL

#convert_JSON_to_EXCEL()

JSON=os.path.join(JSON_dir,'test.json')

print(JSON_dir)



