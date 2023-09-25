class PatientObservation:
    def __init__(self, id_observacao, id_paciente, descricao):
        self.resourceType = "Observation"
        self.id = id_observacao
        self.status = "final"
        self.subject = {
            "reference": f"Patient/{id_paciente}"
        }
        self.note = {
                "text": descricao
        }

    def to_dict(self):
        observation_dict = {
            "resourceType": self.resourceType,
            "id": self.id,
            "status": self.status,
            "subject": self.subject,
            "note": self.note
        }

        return observation_dict
