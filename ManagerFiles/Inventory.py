from distutils.command.clean import clean

import os
from os import scandir, getcwd
from os import walk
class Inventory:
    def __init__(self):
        print("inicializado")

    def structure_directories(self,directories):
        path_relative=[]
        for index , directory in enumerate(directories):
            directory = directory.replace("\\","/")
            is_file=True
            
            if os.path.isdir(directory):  
                is_file=False
                file=""
                folder=directory
            else:
                file=directory.split("/")[len(directory.split("/"))-1]
                folder=directory.replace(file,"")

            if (not directory == self.directory ):
                path_relative.append(
                    {
                        "path-full":directory,
                        "path-relative":directory.replace(self.directory+"/",""),
                        "is_file":is_file,
                        "count-files":0,
                        "folder": folder,
                        "folder-relative": folder.replace(self.directory+"/",""),
                        "file": file
                    }  
                )
        path_relative = self.count_files_folder(path_relative)
        return path_relative         


    def count_files_folder(path):
        count=0
        index_aux=0
        for index,path_relative in enumerate(path):
            if(not path_relative["is_file"]):
                index_aux=index
                count = 0
            else:
                count+=1
                path[index_aux]["count-files"]=count
        return path           

    def get_list_files(self,directory):
        self.directory = directory
        folders=[]
        exceptions=[]
        for folder, dirs, files in os.walk(self.directory):
            add=True
            for exeption in exceptions:
                #se analiza excepciones para saber si hay que profundizar 
                if(folder.find(exeption)>=0):
                    add = False
            if(add):
                folders.append(folder)
                sub_folders=[]
                object_html=False
                for name_file in files:
                    sub_folders.append(folder+"/"+name_file)
                    if (name_file.find(".html")>0):
                        #si es html no profundizamos
                        object_html=True

                if(len(sub_folders)>0):
                    if (not object_html):
                        #agregamos archivos al listado
                        for sub_folder in sub_folders:
                            folders.append(sub_folder)
                    else:
                        exceptions.append(folder)
        inventory = self.structure_directories(self,folders)
        return  inventory