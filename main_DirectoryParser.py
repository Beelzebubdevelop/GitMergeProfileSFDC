import directorycompare
from main_FileParser import fileparser

'''Compare file and merge it in second directory'''
def DirectoryParser(pathdir1,pathdir2):
    for filename in directorycompare.filedirectorycmp(pathdir1,pathdir2):
        try:
            fileparser(filename,pathdir1,pathdir2,pathdir2)
        except Exception:
            print('Some error as Occurred at filename:'+filename)
