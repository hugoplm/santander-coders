from classes_biblioteca.artigo import Artigo
from classes_biblioteca.biblioteca_artigos import Biblioteca_Artigos
from classes_biblioteca.report_similaridade import Report_Similaridade

class Menu():
    def __init__(self):
        self.opcao_usuario = None
        self.nome_biblioteca = 'biblioteca_hugo'
        self.biblioteca = Biblioteca_Artigos(self.nome_biblioteca)
        self.biblioteca_modificada = False
        
        self.__print_menu__()
        
        while self.opcao_usuario != 's':
            self.opcao_usuario = None
            self.__solicitar_opcao__()
            if self.opcao_usuario == '1':
                self.__opcao_cadastro__()
            elif self.opcao_usuario == '2':
                self.__opcao_consulta__()
            elif self.opcao_usuario == '3':
                self.__opcao_report__()
                
        if self.biblioteca_modificada:
            self.biblioteca.salvar_biblioteca()
        
    def __print_menu__(self):
        text_menu = ''
        text_menu += 'Olá, seja bem vindo a Biblioteca de Artigos\n'
        text_menu += 'Veja abaixo as opções disponíveis:\n\n'
        text_menu += '1 - Inserir um novo artigo\n'
        text_menu += '2 - Consultar artigos cadastrados\n'
        text_menu += '3 - Relatório de Similaridade de Artigos'
        
        print(text_menu, flush = True)
            
    def __solicitar_opcao__(self):
        lista_opcoes = ['1', '2', '3', 's']
        while self.opcao_usuario not in lista_opcoes:
            self.opcao_usuario = input('Por favor, digite o número da opção desejada ou "s" para sair')
            if self.opcao_usuario not in lista_opcoes:
                print("Opção inválida.")
            elif self.opcao_usuario.lower() == 's':
                self.opcao_usuario = self.opcao_usuario.lower()
    
    def __opcao_cadastro__(self):
        titulo = input('Insira o título do artigo ')
        
        assunto_valido = None
        while not assunto_valido:
            assunto = input('Insira o assunto do artigo: Esporte, Política ou Tecnologia ')
            assunto_valido = Artigo.validar_assunto(assunto)
            if assunto_valido is False:
                print('Insira um assunto válido')

        data_valida = None
        while not data_valida:
            data = input('Insira a data de publicação do artigo. Formato: AAAA/MM/DD ')
            data_valida = Artigo.validar_data(data)
            if data_valida is False:
                print('Insira uma data válida')

        texto_completo = ''
        texto = input('Insira o texto do artigo ')
        texto_completo = f'{texto_completo} {texto}'
        while texto:
            texto = input('Insira a continuação do texto ou pressione Enter para finalizar.')
            if texto:
                texto_completo = f'{texto_completo} {texto}'
        
        novo_artigo = Artigo(titulo, assunto, data, texto_completo)
        
        self.biblioteca.cadastrar_artigo(novo_artigo.artigo)
        
        self.biblioteca_modificada = True
            
    def __opcao_consulta__(self):
        self.biblioteca.ordenar_biblioteca()
        print(self.biblioteca)
    
    def __opcao_report__(self):
        report = Report_Similaridade(self.biblioteca)
        print(report)