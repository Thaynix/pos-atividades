from xml.dom.minidom import parse

dom = parse("imobiliaria.xml")

cardapio = dom.documentElement

imoveis = cardapio.getElementsByTagName('imovel')

for imovel in imoveis:
    id_do_imovel = imovel.getAttribute('id')
    
    elemento_desc = imovel.getElementsByTagName('descricao')[0]
    descricao = elemento_desc.firstChild.nodeValue
    
    elemento_proprietario = imovel.getElementsByTagName('proprietario')[0]
    nome_proprietario = elemento_proprietario.getElementsByTagName('nome')[0]
    email_proprietario = elemento_proprietario.getElementsByTagName('email')[0]
    telefone_proprietario = elemento_proprietario.getElementsByTagName('telefone')[0]

    elemento_endereco = imovel.getElementsByTagName('endereco')[0]
    rua_endereco = elemento_endereco.getElementsByTagName('rua')[0]
    bairro_endereco = elemento_endereco.getElementsByTagName('bairro')[0]
    cidade_endereco = elemento_endereco.getElementsByTagName('cidade')[0]
    numero_endereco = elemento_endereco.getElementsByTagName('numero')[0]

    elemento_caracteristicas = imovel.getElementsByTagName('caracteristicas')[0]
    tamanho_car = elemento_caracteristicas.getElementsByTagName('caracteristicas')[0]
    num_quartos_car = elemento_caracteristicas.getElementsByTagName('caracteristicas')[0]
    num_banheiros_car = elemento_caracteristicas.getElementsByTagName('caracteristicas')[0]
    numero_car = elemento_caracteristicas.getElementsByTagName('caracteristicas')[0]
    
    

