from AppLoad import AppLoad
from AppTransform import AppTransform
from PatientObservation import PatientObservation
from PatientResource import PatientResource

class AppExtract:
    def __init__(self):
        pass

    def extract_patient(self, dataframe):

        # Inicialize a lista de recursos do Patient
        fhir_pacientes = []

        for indice, linha in dataframe.iterrows():
            # Aplicar transformações usando a classe AppTransform
            transform_genero = AppTransform.mapear_genero(linha['Gênero'])
            transform_ativo = AppTransform.mapear_booleano(True)
            transform_decease = AppTransform.mapear_booleano(False)
            transform_data = AppTransform.transformar_data(linha['Data de Nascimento'])

            # Crie um objeto PatientResource com os dados do paciente
            paciente = PatientResource(
                cpf=str(linha['CPF']),
                nome=str(linha['Nome']),
                genero=transform_genero,
                telefone=str(linha['Telefone']),
                data_nascimento=transform_data,
                pais_nascimento=str(linha['País de Nascimento']),
                ativo=transform_ativo,
                falecido=transform_decease
            )

            fhir_pacientes.append(paciente.to_dict())

        return fhir_pacientes
    
    def extract_observation(self, dataframe):

        # Aplicar transformações usando a classe AppTransform
        dataframe = AppTransform.to_string(dataframe,'Observação')

        # Inicialize a lista de recursos Observation
        fhir_observacoes = []

        for indice, linha in dataframe.iterrows():
            observacao_valor = linha['Observação']

            if observacao_valor != 'nan':

                id_paciente = AppLoad('http://localhost:8080/fhir').get_patient(linha['CPF'])
                if not id_paciente:
                    print(f"Paciente com CPF: {id_paciente} não foi encontrado.")

                descricao = observacao_valor.split("|")
                descricao = ', '.join(descricao)
                # Crie uma instância de PatientObservation
                observacao = PatientObservation(id_observacao=linha['CPF'], id_paciente=id_paciente, descricao=descricao)
                
                fhir_observacoes.append(observacao.to_dict())

        return fhir_observacoes