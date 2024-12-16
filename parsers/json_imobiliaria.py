import json

with open('imobiliaria.json', 'r', encoding='utf-8') as file:
    imoveis = json.load(file)

def exibir_detalhes(imovel):
    print("\nDetalhes do Imóvel:")
    print(f"Descrição: {imovel['descricao']}")
    print("Proprietário:")
    print(f"  Nome: {imovel['proprietario']['nome']}")
    if imovel['proprietario']['emails']:
        print(f"  Emails: {', '.join(imovel['proprietario']['emails'])}")
    else:
        print("  Emails: N/A")
    print(f"  Telefones: {', '.join(imovel['proprietario']['telefones'])}")
    print("Endereço:")
    print(f"  Rua: {imovel['endereco']['rua']}")
    print(f"  Bairro: {imovel['endereco']['bairro']}")
    print(f"  Cidade: {imovel['endereco']['cidade']}")
    numero = imovel['endereco']['numero'] or 'N/A'
    print(f"  Número: {numero}")
    print("Características:")
    print(f"  Tamanho: {imovel['caracteristicas']['tamanho']}")
    print(f"  Número de Quartos: {imovel['caracteristicas']['numQuartos']}")
    print(f"  Número de Banheiros: {imovel['caracteristicas']['numBanheiros']}")
    print(f"Valor: {imovel['valor']}")



print("\n Menu de Imóveis ")
for imovel in imoveis:
    print(f"{imovel['id']}. {imovel['descricao']}")

escolha = int(input("\nDigite o id do imovel: "))

for imovel in imoveis:
    if imovel['id'] == escolha:
        exibir_detalhes(imovel)
        break
    else:
        print("ID inválido. Por favor, tente novamente.")
