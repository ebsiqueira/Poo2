import json

contatos = {}
contatos['Mateus'] = '1111-0000'
contatos['Victor'] = '2222-3333'
f = open('listaTelefonica.json', 'w')
json.dump(contatos, f)
f.close()