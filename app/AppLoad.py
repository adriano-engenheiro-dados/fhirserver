import json
import requests

class AppLoad:
    def __init__(self, url_servidor_fhir):
        self.url_servidor_fhir = url_servidor_fhir

    def send_endpoint(self, fhir_recursos):
        for recurso_fhir in fhir_recursos:
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/fhir+json"  # Especifica o formato de aceitação FHIR
            }
            resource_type = recurso_fhir['resourceType']
            identifier_obj = recurso_fhir['identifier'] if resource_type == 'Patient' else recurso_fhir['subject']
            response = requests.post(self.url_servidor_fhir, data=json.dumps(recurso_fhir), headers=headers)

            if response.status_code == 201:
                print(f"{resource_type} Resource FHIR criado com sucesso. ID: {response.json().get('id')}. Identificador: {identifier_obj}")
            else:
                print(f"Erro ao criar {resource_type} Resource FHIR. Status: {response.status_code}. Paciente: {identifier_obj} ")

    def get_patient(self, identifier):

        resource_type = "Patient"

        query_params = {"identifier": identifier}

        response = requests.get(f"{self.url_servidor_fhir}/{resource_type}", params=query_params)

        if response.status_code == 200:
            paciente = response.json().get("entry", [{}])[0].get("resource", {}).get("id")
        else:
            print(f"Erro ao buscar paciente. Status: {response.status_code}")
        
        return paciente