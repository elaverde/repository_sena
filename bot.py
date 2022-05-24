from asyncio import exceptions
from itertools import count
import os
import time
from ManagerFiles import Inventory, Excel, Repository


def inventary(folderPath):
    folderPath = folderPath.replace("\\", "/")

    repository = Repository
    xls = Excel
    xls.created_file(xls)
    xls.write_cell(xls,"A3","Ruta")
    xls.write_cell(xls,"B3","Archivo")
    xls.write_cell(xls,"C3","Fecha")
    xls.write_cell(xls,"D3","Peso")

    xls.set_width_column(xls,"A",40)
    xls.set_width_column(xls,"B",60)
    xls.set_width_column(xls,"C",20)
    xls.set_width_column(xls,"D",20)


    countRowA=4
    countRowB=4
    
    inventory = Inventory
    Directories = inventory.get_list_files(inventory,folderPath)


    for obj in Directories:
        if(not obj["is_file"]):
            xls.write_cell(xls,"A"+str(countRowA),str(obj["folder-relative"]))
            if(obj["count-files"]>1):
                mergeCount = (obj["count-files"] + countRowA)-1
                xls.merge_cell(xls,"A"+str(countRowA),"A"+str(mergeCount))
                xls.center_cell(xls,"A"+str(countRowA))
                countRowA = (mergeCount)
            else:
                xls.write_cell(xls,"B"+str(countRowB),str(obj["file"]))
                xls.write_cell(xls,"C"+str(countRowB),str(repository.get_last_update_repository(repository,obj["path-full"])))
                xls.write_cell(xls,"D"+str(countRowB),str(repository.size(repository,obj["path-full"])))
                countRowB += 1
            countRowA += 1 
        else:
            aux_file = obj["path-full"].replace(folderPath+"/","")
            if (aux_file==obj["file"]):
                xls.write_cell(xls,"A"+str(countRowA),str(aux_file))
                xls.write_cell(xls,"C"+str(countRowA),str(repository.get_last_update_repository(repository,obj["path-full"])))
                xls.write_cell(xls,"D"+str(countRowA),str(repository.size(repository,obj["path-full"])))
                countRowA += 1
                countRowB += 1
            else:
                xls.write_cell(xls,"B"+str(countRowB),str(obj["file"]))
                xls.write_cell(xls,"C"+str(countRowB),str(repository.get_last_update_repository(repository,obj["path-full"])))
                xls.write_cell(xls,"D"+str(countRowB),str(repository.size(repository,obj["path-full"])))
                countRowB += 1  
    xls.save_file(xls,folderPath+"/reporte.xls")
    print("El inventario se ha generado en la carpeta: "+folderPath+"/reporte.xls")
def menu():
    print("$ Por favor ingrese la carpeta a inventariar:")
    folderPath = input("$_ ")
    inventary(folderPath)
    menu()
if __name__ == "__main__":
    menu()