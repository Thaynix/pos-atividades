import zeep

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
client = zeep.Client(wsdl=wsdl_url)
id_pais = "NO"
resultado = client.service.CapitalCity(sCountryISOCode=id_pais)

print(f"A capital de ({id_pais}) = Noruega é {resultado} :D")