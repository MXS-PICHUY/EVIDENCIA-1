from os import mkdir
from os.path import exists

destination = "C:/Programacion/"
pl  = "2doSemestre"

if exists(destination):
    print ("ya existe el directorio")
else:
    mkdir(destination)
    mkdir(destination+pl)
    destSubfolder = destination+pl