import zeep

wsdl_url = 'https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL'
client = zeep.Client(wsdl=wsdl_url)
num = input('digite numerinhos pfv: ')
resultado = client.service.NumberToWords(ubiNum=num)

print(f"esse é o numero q voce digitou escrito em ingles :V : {resultado.title()}")