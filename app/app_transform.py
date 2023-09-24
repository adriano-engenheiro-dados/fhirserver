from datetime import datetime

class AppTransform:
    @staticmethod
    def mapear_genero(genero):
        if genero == 'Masculino':
            return 'male'
        elif genero == 'Feminino':
            return 'female'
        else:
            return genero

    @staticmethod
    def mapear_booleano(valor):
        return str(valor).lower()

    @staticmethod
    def transformar_data(data_str):
        return datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%d")
