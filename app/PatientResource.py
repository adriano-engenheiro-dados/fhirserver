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
        #Calcular o positivo do modelo. Este PatientResource possui 18 campos, mas apenas 10 atributos.
        self.percentual_preenchido = (lambda x, y: (x / y) * 100)(10, 18)

    def to_dict(self):

        fhir_paciente = {
            "resourceType": "Patient",
            "extension": [
                {
                    "url": "birthCountry",
                    "valueString": self.pais_nascimento
                },
                {
                    "url": "registerQuality",
                    "positiveInt": self.percentual_preenchido
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
