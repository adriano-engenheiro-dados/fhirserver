class PatientResource:
    def __init__(self, cpf, nome, genero, telefone, data_nascimento, pais_nascimento, ativo, falecido):
        self.ativo = ativo
        self.falecido = falecido
        self.id = cpf
        self.cpf = cpf
        self.nome = nome
        self.genero = genero
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.pais_nascimento = pais_nascimento

    def to_dict(self):

        fhir_paciente = {
            "resourceType": "Patient",
            "id": self.cpf,
            "extension": [
                {
                    "url": "birthCountry",
                    "valueString": self.pais_nascimento
                },
                {
                    "url": "registerQuality",
                    "positiveInt": 80
                }
            ],
            "identifier": [
                {
                    "value": self.cpf
                }
            ],
            "active": self.ativo,
            "name": [
                {
                    "given": self.nome
                }
            ],
            "telecom": [
                {
                    "system": "phone",
                    "value": self.telefone
                }
            ],
            "gender": self.genero,
            "birthDate": self.data_nascimento,
            "deceasedBoolean": self.falecido,
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

        return fhir_paciente
