import profileparser
import objectdefinition

def generatexml(inputlist):
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

# def generatexml(merged):
#     for elem in merged:
#         root = etree.Element(elem.instancename())
#         if objectdefinition.oneLineTag(elem): #Single Tag
#             root.text = testelement[elem.tag] = 
#         for subelem in elem:
#             testelement[subelem.tag] = subelem.text
#         mylist.append(testelement)

#     root = etree.Element('root')
#     root.append(etree.Element('child'))
#     # another child with text
#     child = etree.Element('child')
#     child.text = 'some text'
#     root.append(child)

#     # pretty string
#     return etree.tostring(root, pretty_print=True)

# def createxml(qualcosa):
#     E = lxml.builder.ElementMaker()
#     ROOT = E.root
#     DOC = E.doc
#     FIELD1 = E.field1
#     FIELD2 = E.field2

#     the_doc = ROOT(
#             DOC(
#                 FIELD1('some value1', name='blah'),
#                 FIELD2('some value2', name='asdfasd'),
#                 )   
#             )   

#     print lxml.etree.tostring(the_doc, pretty_print=True)