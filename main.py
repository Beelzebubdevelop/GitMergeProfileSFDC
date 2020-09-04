from profileparser import parse
from comparator import compare
from xmlgenerator import generatexml
from writerutils import writeonfile

try:
    path1 = input('Inserisci qua il primo pathname:')
    path2 = input('Inserisci qua il secondo pathname:')
    parse1 = parse(path1)
    parse2 = parse(path2)
    merged = compare(parse1,parse2)
    outputxml = generatexml(merged)
    outputpath = input('Inserisci qua il path di output:')
    filename = input('Inserisci qua il nome del file di output:')
    writeonfile(outputxml,outputpath,filename)

except Exception:
    print('Some error as Occurred')