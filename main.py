from asyncio import exceptions
from itertools import count
import os
from ManagerFiles import Folders, Inventory, Excel

managerFolder = Folders
xls = Excel
xls.created_file(xls)
xls.write_cell(xls,"A3","Ruta")
xls.write_cell(xls,"B3","Archivo")
xls.write_cell(xls,"C3","Fecha")
xls.write_cell(xls,"D3","Peso")

countRow=4
countRowFile=4


folderPath="C:/apps/tool/228118"
folders = os.listdir(folderPath)

for folder in folders:
    print(folder, managerFolder.size_folder(folderPath + "/" + folder))

inventory = Inventory

cleanDirectories,countD = inventory.get_list_files(inventory,folderPath)


for obj in countD:
    xls.write_cell(xls,"A"+str(countRow),str(obj["name"]))
    if(obj["count"]>1):

        mergeCount = (obj["count"] + countRow)-1
        xls.merge_cell(xls,"A"+str(countRow),"A"+str(mergeCount))
        xls.center_cell(xls,"A"+str(countRow))
        countRow=mergeCount
        #reporte archios
        for f in cleanDirectories:
            file=f["path-relative"].replace(str(obj["name"]),'')
            if not file.startswith('/'): 
                file = "/" + file
            xls.write_cell(xls,"B"+str(countRowFile),str(file))
            countRowFile += 1
            #print(f["path-full"])
            #print(f["path-relative"])
    
    countRow += 1


xls.save_file(xls,"./reporte.xls")
print(countD)
