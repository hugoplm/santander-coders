class Biblioteca_Artigos():
    def __init__(self, nome):
        self.nome = nome
        self.nome_arquivo = f'{self.nome}.csv'
        self.artigos = self.__carregar_lista_artigos__()
                    
    def __carregar_dados_arquivo__(self):
        dados = None
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                dados = arquivo.readlines()
        except FileNotFoundError:
            self.__criar_novo_arquivo__()
        return dados
    
    def __formatar_lista_artigos__(self, dados):
        if dados:
            dados.pop(0)
            lista_artigos = [linha.split(';') for linha in dados]
            for artigo in lista_artigos:
                artigo.remove('\n')
        else:
            lista_artigos = []
        return lista_artigos
        
    def __carregar_lista_artigos__(self):
        dados = self.__carregar_dados_arquivo__()
        lista_artigos = self.__formatar_lista_artigos__(dados)
        return lista_artigos

    def __index_arquivo_existente__(self, artigo):
        titulo = artigo[0]
        for index, item in enumerate(self.artigos):
            if item[0] == titulo:
                return index
        return None

    def cadastrar_artigo(self, artigo):
        index_artigo = self.__index_arquivo_existente__(artigo)

        if index_artigo is None:
            self.artigos.append(artigo)
            print('Artigo cadastrado com sucesso')
        else:
            sobrescrever = None
            lista_opcoes = ['s', 'n']
            while sobrescrever not in lista_opcoes:
                sobrescrever = input('Título já cadastrado na biblioteca. Deseja sobrescrever? Digite S ou N')
                if sobrescrever.lower() not in lista_opcoes:
                    print('Opção inválida.')
                elif sobrescrever.lower() == 's':
                    self.artigos[index_artigo] = artigo
                    print('Artigo atualizado com sucesso')
                else:
                    print('Artigo não cadastrado.')

    def __criar_novo_arquivo__(self):
        cabecalho = 'Titulo;Assunto;Data Publicacao;Texto;\n'
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write(cabecalho)
    
    def salvar_biblioteca(self):
        self.__criar_novo_arquivo__()
        with open(self.nome_arquivo, 'a') as arquivo:
            for item in self.artigos:
                linha_csv = ";".join(item) + ';\n'
                arquivo.write(linha_csv)
                
    def ordenar_biblioteca(self):
        self.artigos = sorted(self.artigos, key=lambda artigo: artigo[2], reverse=True)
    
    def __repr__(self):
        c_data = 'Data de Publicação'
        c_assunto = 'Assunto'
        c_titulo = 'Título'
        
        text = f' {c_data:18} | {c_assunto:10} | {c_titulo:50} \n'
        for artigo in self.artigos:
            text += f' {artigo[2]:18} | {artigo[1]:10} | {artigo[0][:80]} \n'
        return text