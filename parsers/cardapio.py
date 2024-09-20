from xml.dom.minidom import parse

dom = parse("cardapio.xml")

# Elemento raiz do XML (biblioteca)
cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "livro"
pratos = cardapio.getElementsByTagName('prato')

# Acessa as informações de cada livro
for prato in pratos:
    id_do_prato = prato.getAttribute('id')
    elemento_nome = prato.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    elemento_desc = prato.getElementsByTagName('descricao')[0]
    descricao = elemento_desc.firstChild.nodeValue
    elemento_ings = prato.getElementsByTagName('ingrediente')
    for elemento_ing in elemento_ings:
        ingredientes = elemento_ing.firstChild.nodeValue
        print("Ingredientes:", ingredientes)    
    
    print("Nome do prato:", nome)
    print("Descricao do prato:", descricao)
    