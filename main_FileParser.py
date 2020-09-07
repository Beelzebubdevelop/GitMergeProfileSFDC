from profileparser import parse
from comparator import compare
from xmlgenerator import generatexml
from writerutils import writeonfile

def fileparser(filename,path1,path2,outputpath):
    try:
        parse1 = parse(path1+'/'+filename)
        parse2 = parse(path2+'/'+filename)
        merged = compare(parse1,parse2)
        outputxml = generatexml(merged)
        writeonfile(outputxml,outputpath,'/'+filename)

    except Exception as e:
        print(e)
        # print('filename: ',filename,' path1: ',path1,' path2: ',path2,' outputpath: ',outputpath)