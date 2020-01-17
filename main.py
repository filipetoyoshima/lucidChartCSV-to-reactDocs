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
        componentName = row['Área de texto 1'].split('/', 1)[0]
        componentName = ''.join(e for e in componentName if e.isalnum())

        components.append({
            'id': row['Id'],
            'name': componentName,
            'childs': [],
            'importedOn': [],
        })
    elif row['Nome'] == 'Linha':
        originId = find(components, 'id', row['Origem da linha'])
        destinyId = find(components, 'id', row['Destino da linha'])

        components[originId]['childs'].append(components[destinyId]['name'])
        components[destinyId]['importedOn'].append(components[originId]['name'])

comentsBlock = ''
print(components)

for component in components:
    childList = ''
    for child in component['childs']:
        childList += ' * - [{}](#{})\n'.format(child, child.lower())
    
    importedOnList = ''
    for importedOn in component['importedOn']:
        importedOnList += ' * - [{}](#{})\n'.format(importedOn, importedOn.lower())

    

    example = """\
Exemplo:
```js
<{}/>
```
    """.format(component['name'])
    print(example)
    
    comment = """
---------------------
Componente: {}

/**
 * Filhos:
{} *
 * Importado em:
{} */
    """.format(component['name'], childList, importedOnList)

    comentsBlock += comment


    myFile = open('docs/{}.md'.format(component['name']), 'w')
    myFile.write(example)
    myFile.close()

myFile = open('list.md', 'w')
myFile.write(comentsBlock)
myFile.close()