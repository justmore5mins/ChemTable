from json import dump,dumps,load
from Errors.commanderror import *

fileread = open("/Users/AustinYu/Library/CloudStorage/GoogleDrive-tno062789@gmail.com/我的雲端硬碟/python/ChemTable/Data/elems.json","r")
filewrite = open("/Users/AustinYu/Library/CloudStorage/GoogleDrive-tno062789@gmail.com/我的雲端硬碟/python/ChemTable/Data/elems.json","w")

import json

def remove_last_character_from_json_file():
    json_data = json.load(fileread)

    # 將 JSON 轉成字串
    json_string = json.dumps(json_data)

    # 刪除最後一個字元
    json_string = json_string[:-1]

    # 將字串轉回 JSON
    json_data = json.loads(json_string)

    # 將 JSON 寫回檔案
    json.dump(json_data, filewrite)


def addElements(Element_Symbol:str,Element_English_name:str,Atom_Number:int, Element_Characteristics:str = "",Element_Characteristics_Chinese:str = ""):
  
    atom_number = str(Atom_Number)
  
    if Element_Characteristics == "":
        Element_Characteristics:None
    
    if Element_Characteristics_Chinese == "":
        Element_Characteristics_Chinese:None
  
    element_data = {Element_Symbol:{"English name":Element_English_name,"Atom number":atom_number,"Element Characteristics English":Element_Characteristics,"Element Characteristics Chinese":Element_Characteristics_Chinese}}
    rawdatas = load(fileread)
    rawdatas[Element_Symbol] = element_data
    dump(element_data,filewrite,indent=2)
        
addElements("He","Helium","2")