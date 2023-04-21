from json import dump,dumps
from time import sleep as delay
from Errors.commanderror import *

def addElements(Element_Symbol:str,Element_English_name:str,Element_Chinese_name:str,Atom_Number:int, Element_Characteristics:str = "",Element_Characteristics_Chinese:str = ""):
    element_data = {"English name":Element_English_name,"Chinese name":Element_Chinese_name,"Atom number":Atom_Number,"Element Characteristics English":Element_Characteristics,"Element Characteristics Chinese":Element_Characteristics_Chinese}
    Element_Data = {"Symbol":Element_Symbol}
    delay(10)
    try:
        dump()
    except:
        raise CommandsError("There's some error when writing data to elements data")
        
addElements("H","Hydrogen","氫","1")