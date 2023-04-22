from json import dump,load,JSONDecoder
from Errors.commanderror import *

filepath = "/Users/AustinYu/Library/CloudStorage/GoogleDrive-tno062789@gmail.com/我的雲端硬碟/python/ChemTable/Data/elems.json"

def addElements(Element_Symbol:str,Element_English_name:str,Atom_Number:int,Valence:int,Atom_mass: float, Element_Characteristics:str = ""):
  
    if Atom_mass > 0:
        pass
    else:
        raise ValueError("Mass con't be -")
  
    element_data = {Element_Symbol:{"English name":Element_English_name,"Atom number":Atom_Number,"Valence":Valence,"Atom Mass":Atom_mass,"Element Characteristics English":Element_Characteristics}}
    
    with open(filepath,"r",encoding="utf-8") as file:
        data = load(file)
        
        data.update(element_data)
        
    with open(filepath,"w",encoding="utf-8") as filewrite:
        dump(data,filewrite,indent=2)
   
while True:
    Element_Symbol = input("請輸入元素符號: ")
    Element_English_name = input("請輸入元素的英文名稱: ")
    Atom_Number = int(input("請輸入原子序: "))
    Valence = int(input("請輸入價數: "))
    Atom_mass = float(input("請輸入原子質量: "))
    addElements(Element_Symbol=Element_Symbol,Element_English_name=Element_English_name,Atom_Number=Atom_Number,Valence=Valence,Atom_mass=Atom_mass)
    print('\n')