import objectdefinition

'''This method concatenate two list and avoid duplicate'''
def compare(firstlist,secondlist):
    joined_list = [*firstlist,*secondlist]
    return list({v[v.key()]:v for v in joined_list}.values()) #Questo toglie tutti i duplicati, ma fa vincere sempre l'oggetto della seconda lista