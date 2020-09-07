from main_FileParser import fileparser

try:
    filename = input('Inserisci qua il nome del file:')
    path1 = input('Inserisci qua il path della prima directory:')
    path2 = input('Inserisci qua il path della seconda directory:')
    outputpath = input('Inserisci qua il path di output:')
    
    fileparser(filename,path1,path2,outputpath)

except Exception:
    print('Some error as Occurred')