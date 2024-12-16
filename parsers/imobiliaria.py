import json
from xml.dom.minidom import parse

dom = parse("imobiliaria.xml")

imobiliaria = dom.documentElement

imoveis = imobiliaria.getElementsByTagName("imovel")

imoveis_lista = []
id_imovel = 0

for imovel in imoveis:
    id_imovel += 1
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue

    proprietario_element = imovel.getElementsByTagName("proprietario")[0]
    nome_proprietario = proprietario_element.getElementsByTagName("nome")[0].firstChild.nodeValue
    emails = [email.firstChild.nodeValue for email in proprietario_element.getElementsByTagName("email")]
    telefones = [telefone.firstChild.nodeValue for telefone in proprietario_element.getElementsByTagName("telefone")]

    endereco_element = imovel.getElementsByTagName("endereco")[0]
    rua = endereco_element.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = endereco_element.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = endereco_element.getElementsByTagName("cidade")[0].firstChild.nodeValue
    numero_elements = endereco_element.getElementsByTagName("numero")
    numero = numero_elements[0].firstChild.nodeValue if numero_elements else None

    caracteristicas_element = imovel.getElementsByTagName("caracteristicas")[0]
    tamanho = caracteristicas_element.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    num_quartos = caracteristicas_element.getElementsByTagName("numQuartos")[0].firstChild.nodeValue
    num_banheiros = caracteristicas_element.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue

    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue

    imovel_dict = {
        "id": id_imovel,
        "descricao": descricao,
        "proprietario": {
            "nome": nome_proprietario,
            "emails": emails,
            "telefones": telefones,
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero,
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": num_quartos,
            "numBanheiros": num_banheiros,
        },
        "valor": valor,
    }

    imoveis_lista.append(imovel_dict)

json_output = json.dumps(imoveis_lista, indent=4, ensure_ascii=False)

with open("imobiliaria.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_output)
