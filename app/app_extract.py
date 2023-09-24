import json
import pandas as pd
import requests
from app_transform import AppTransform

# URL do arquivo CSV
url_csv = "https://raw.githubusercontent.com/wandersondsm/teste_fhir/main/data/patients.csv"

# Lê o arquivo CSV diretamente da URL
df = pd.read_csv(url_csv, encoding='ISO-8859-1')

# Inicialize a lista de recursos FHIR
fhir_recursos = []

for indice, linha in df.iterrows():
    # Aplicar transformações usando a classe AppTransform
    transform_genero = AppTransform.mapear_genero(linha['Gênero'])
    transform_ativo = AppTransform.mapear_booleano(True)
    transform_decease = AppTransform.mapear_booleano(False)
    transform_data = AppTransform.transformar_data(linha['Data de Nascimento'])

    recurso_fhir = {
                    "resourceType": "Patient",
                    "extension": [
                        {
                            "url": "birthCountry",
                            "valueString": str(linha['País de Nascimento'])
                        },
                        {
                            "url": "registerQuality",
                            "positiveInt": 80
                        }
                    ],
                    
                    "identifier": [
                        {
                            "value": str(linha['CPF'])
                        }
                    ],
                    "active": transform_ativo,
                    "name": [
                        {
                            "given": str(linha['Nome'])
                        }
                    ],
                    "telecom": [
                        {
                            "system": "phone",
                            "value": str(linha['Telefone'])
                        }
                    ],
                    "telecom": str(linha['Telefone']),
                    "gender": transform_genero,
                    "birthDate": transform_data,
                    "deceasedBoolean": transform_decease,
                    "address": [
                        {
                            "use": "",
                            "type": "",
                            "line": "",
                            "city": "",
                            "state": "",
                            "postalCode": ""
                        }
                    ]
                }

    fhir_recursos.append(recurso_fhir)

# URL do servidor FHIR
url_servidor_fhir = "http://localhost:8080/fhir/Patient"  # Substitua pelo URL correto

# Envia os recursos FHIR para o servidor
for recurso_fhir in fhir_recursos:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/fhir+json"  # Especifica o formato de aceitação FHIR
    }
    response = requests.post(url_servidor_fhir, data=json.dumps(recurso_fhir), headers=headers)

    if response.status_code == 201:
        print(f"Patient Resource FHIR criado com sucesso. ID: {response.json().get('identifier')}")
    else:
        print(f"Erro ao criar recurso FHIR. Status: {response.status_code}")
