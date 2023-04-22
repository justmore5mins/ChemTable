from json import dump,dumps,load
from Errors.commanderror import *

filepath = "/Users/AustinYu/Library/CloudStorage/GoogleDrive-tno062789@gmail.com/我的雲端硬碟/python/ChemTable/Data/elems.json"

def addElements(Element_Symbol:str,Element_English_name:str,Atom_Number:int, Element_Characteristics:str = "",Element_Characteristics_Chinese:str = ""):
    atom_number = str(Atom_Number)
    
    if Element_Characteristics == "":
        Element_Characteristics:None
    
    if Element_Characteristics_Chinese == "":
        Element_Characteristics_Chinese:None
  
    element_data = {Element_Symbol:{"English name":Element_English_name,"Atom number":atom_number,"Element Characteristics English":Element_Characteristics,"Element Characteristics Chinese":Element_Characteristics_Chinese}}
    with open(filepath,"a+",encoding="utf-8") as filewrite:
        data = filewrite.read()
        data = str(data)
        data = data[:-2]
        data = data+ ","
        filewrite.write("\n")
    
    with open(filepath,"w",encoding="utf-8") as file:
        file.write(data)
        
    with open(filepath,"a+",encoding="utf-8") as file:
        dump(element_data,file,indent=2)

#addElements("H","hydrogen",2)
addElements("He","Helium","2")