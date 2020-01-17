import pandas as pd

def isInArray(componentName, components):
    for obj in componentName:
        if componentName == obj['name']:
            return True
    return False


def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1


data = pd.read_csv("componentGraph.csv")

print(data)

components = []

for index, row in data.iterrows():
    if row['Nome'] == 'Processo':
        components.append({
            'id': row['Id'],
            'name': row['Área de texto 1'],
            'childs': [],
            'importedOn': [],
        })
    elif row['Nome'] == 'Linha':
        originId = find(components, 'id', row['Origem da linha'])
        destinyId = find(components, 'id', row['Destino da linha'])

        components[originId]['childs'].append(components[destinyId]['name'])
        components[destinyId]['importedOn'].append(components[originId]['name'])

for component in components:
    childList = ''
    for child in component['childs']:
        childList += ' * - {}\n'.format(child)
    
    importedOnList = ''
    for importedOn in component['importedOn']:
        importedOnList += ' * - {}\n'.format(importedOn)

    s = """
------------
# Componente: {}

/**
 * Filhos:
{} *
 * Importado em:
{} */
    """.format(component['name'], childList, importedOnList)

    print(s)