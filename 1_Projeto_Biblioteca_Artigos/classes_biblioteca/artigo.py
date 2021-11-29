class Artigo():
    def __init__(self, titulo, assunto, data_publicacao, texto):
        self.titulo = titulo
        self.assunto = assunto.capitalize()
        self.data_publicacao = data_publicacao
        self.texto = texto
        self.artigo = [self.titulo, self.assunto, self.data_publicacao, self.texto]

    @staticmethod
    def validar_assunto(assunto):
        lista_assuntos = ['esporte', 'política', 'tecnologia']
        return assunto.lower() in lista_assuntos
    
    @staticmethod
    def validar_data(data):
        tam_val = len(data) == 10

        ano = data[0:4]
        ano_val = ano.isnumeric() and int(ano) > 0
        
        primeira_barra = data[4]
        p_bar_val = primeira_barra == "/"
        
        mes = data[5:7]
        mes_val = mes.isnumeric() and 1 <= int(mes) <= 12
        
        segunda_barra = data[7]
        s_bar_val = segunda_barra == "/"
        
        dia = data[8:]
        dia_val = dia.isnumeric() and 1 <= int(dia) <= 31
        return (tam_val and ano_val and p_bar_val and mes_val and s_bar_val and dia_val)
