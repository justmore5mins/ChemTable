from json import dump

file = open("/Users/AustinYu/Library/CloudStorage/GoogleDrive-tno062789@gmail.com/我的雲端硬碟/python/ChemTable/test/test.json","w+")

dump({"Hello World":1,"Hello Python":{"WTF":"Hello"}},file,indent=2)