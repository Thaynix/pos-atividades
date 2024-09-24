from xml.dom.minidom import parse

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

def menu():
    for prato in pratos:
        id_prato = prato.getAttribute('id')
        nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue

        print(f"{id_prato} {nome}")

menu()
menu = input("qual vose qr? ")

for prato in pratos:
    id_do_prato = prato.getAttribute('id')
    
    elemento_nome = prato.getElementsByTagName('nome')[0]
    nome = elemento_nome.firstChild.nodeValue
    
    elemento_desc = prato.getElementsByTagName('descricao')[0]
    descricao = elemento_desc.firstChild.nodeValue
    
    elemento_preco = prato.getElementsByTagName('preco')[0]
    preco = elemento_preco.firstChild.nodeValue
    
    elemento_cal = prato.getElementsByTagName('calorias')[0]
    cal = elemento_cal.firstChild.nodeValue
    
    elemento_tempprep = prato.getElementsByTagName('tempoPreparo')[0]
    tempprep = elemento_tempprep.firstChild.nodeValue

    elemento_ings = prato.getElementsByTagName('ingrediente')
    
    if id_do_prato == menu:
        print("Nome do prato:", nome)
        print("Descricao do prato:", descricao)
        print("Preço:", preco)
        print("Calorias", cal)
        print("Tempo de Preparo:", tempprep)

        for elemento_ing in elemento_ings:
            ingredientes = elemento_ing.firstChild.nodeValue
            print("Ingredientes:", ingredientes)

