from AppExtract import AppExtract
from AppLoad import AppLoad
import pandas as pd

# URL do arquivo CSV
url_csv = "https://raw.githubusercontent.com/wandersondsm/teste_fhir/main/data/patients.csv"
df = pd.read_csv(url_csv, encoding='ISO-8859-1')

# Extrai pacientes do arquivo
fhir_patients = AppExtract().extract_patient(df)

# Crie uma instância de AppLoad com a URL para o objeto PatientResource
AppLoad("http://localhost:8080/fhir/Patient").send_endpoint(fhir_patients)

# Extrai Observações dos Pacientes no arquivo
fhir_obs = AppExtract().extract_observation(df)

# Crie uma instância de AppLoad com a URL para o objeto Observation
AppLoad("http://localhost:8080/fhir/Observation").send_endpoint(fhir_obs)
