import pandas as pd
import xmltodict
import json

def XmlToJson(file):
    obj = xmltodict.parse(file)
    jsondata = json.dumps(obj)
    return jsondata

def XlsxToJson(file):
    excel_df= pd.read_excel(file)
    jsondata = excel_df.to_json()
    return jsondata
    
def CsvToJson(file):
    df = pd.read_csv(file)
    jsonData = df.to_json()

    return jsonData

def writetofile(filename,data):
    name =  filename.name.split('.')[0]
    filepath = f'media/{name}.json'
    with open(filepath,'w') as jsonfile:
        jsonfile.write(data)
    
    return filepath