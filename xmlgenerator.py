import profileparser
import objectdefinition

def generatexml(inputlist):
    inputlist.sort()
    output = docstart()
    for elem in inputlist:
        print('elem: ',elem)
        if objectdefinition.oneLineTag(elem): #Single Tag
            output += roottagvalue(elem.instancename(),elem[elem.key()])
        else:
            output += openroottag(elem.instancename())
            for (key,value) in elem:
                print('subelem: ',(key,value))
                output += childtag(key,value)
            output += closeroottag(elem.instancename())
    output += docend()
    return output



def docstart():
    return '<?xml version="1.0" encoding="UTF-8"?>\n<Profile xmlns="http://soap.sforce.com/2006/04/metadata">\n'

def docend():
    return '</Profile>'

def openroottag(name):
    return '\t<'+name+'>\n'

def closeroottag(name):
    return '\t</'+name+'>\n'

def roottagvalue(name,value):
    return '\t<'+name+'>'+value+'</'+name+'>\n'

def childtag(name,value):
    return '\t\t<'+name+'>'+value+'</'+name+'>\n'
