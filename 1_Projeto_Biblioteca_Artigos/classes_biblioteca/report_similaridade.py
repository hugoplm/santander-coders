class Report_Similaridade():
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.artigos_similares = self.__definir_mais_similares__()
    
    def __remover_pontuacao__(self, texto):
        texto_formatado = (
            texto
            .lower()
            .replace(',', '')
            .replace('.', '')
            .replace('!', '')
            .replace('?', '')
            .replace('\n', ' ')
            .replace('(', '')
            .replace(')', ' ')
        )
        return texto_formatado
                    
    def __remover_stopwords__(self, texto):
        lista_stopwords = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é', 
                            'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 
                            'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu', 
                            'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está', 
                            'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 
                            'era', 'depois', 'sem', 'mesmo', 'aos', 'ter', 'seus', 'quem', 'nas', 
                            'me', 'esse', 'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 
                            'nem', 'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas', 
                            'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles', 'essas', 
                            'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te', 'vocês', 'vos', 
                            'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 
                            'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 
                            'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 
                            'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 
                            'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 
                            'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 
                            'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 
                            'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 
                            'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 
                            'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 
                            'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 
                            'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 
                            'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 
                            'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 
                            'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 
                            'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 
                            'teríamos', 'teriam']
        
        lista_texto_formatado = texto.split()
        
        for palavra in lista_texto_formatado:
            if palavra in lista_stopwords:
                lista_texto_formatado.remove(palavra)
        return lista_texto_formatado
        
    def __definir_palavras_unicas__(self, lista_texto):
        lista_texto_ordenada = sorted(lista_texto)
        lista_palavras_unicas = []
        
        palavra_anterior = ''
        for palavra in lista_texto_ordenada:
            if palavra != palavra_anterior:
                lista_palavras_unicas.append(palavra)
            palavra_anterior = palavra
        return lista_palavras_unicas
    
    def __calcular_metrica_similaridade__(self, texto_1, texto_2):
        t1_pont = self.__remover_pontuacao__(texto_1)
        t2_pont = self.__remover_pontuacao__(texto_2)
        
        t1_swords = self.__remover_stopwords__(t1_pont)
        t2_swords = self.__remover_stopwords__(t2_pont)
        
        t1_punicas = self.__definir_palavras_unicas__(t1_swords)
        t2_punicas = self.__definir_palavras_unicas__(t2_swords)
        
        punicas_t1_t2 = self.__definir_palavras_unicas__(t1_punicas + t2_punicas)
        total_punicas_t1_t2 = len(punicas_t1_t2)
        
        quantidade_p_coincidente = 0
        
        for palavra in t1_punicas:
            if palavra in t2_punicas:
                quantidade_p_coincidente += 1
        
        resultado_similaridade = (quantidade_p_coincidente) / (total_punicas_t1_t2)
        return resultado_similaridade
        
    def __definir_mais_similares__(self):
        quantidade_artigos = len(self.biblioteca.artigos)
        
        if quantidade_artigos < 2:
            return ['Quantidade de artigos insuficiente na biblioteca.']
        else:
            max_similaridade = 0
            posicao_max_similaridade = ()

            for i in range(quantidade_artigos):
                for j in range(i + 1, quantidade_artigos):
                    texto_i = self.biblioteca.artigos[i][3]
                    texto_j = self.biblioteca.artigos[j][3]
                    similaridade = self.__calcular_metrica_similaridade__(texto_i, texto_j)
                    if similaridade > max_similaridade:
                        max_similaridade = similaridade
                        posicao_max_similaridade = i, j
            
            if len(posicao_max_similaridade) < 2:
                return ['Não existem artigos similares na biblioteca.']
            else:
                mais_similar_1 = self.biblioteca.artigos[posicao_max_similaridade[0]][0]
                mais_similar_2 = self.biblioteca.artigos[posicao_max_similaridade[1]][0]
                return [mais_similar_1, mais_similar_2]
        
    def __repr__(self):
        if len(self.artigos_similares) < 2:
            text = self.artigos_similares[0]
        else:
            mais_similar_1 = self.artigos_similares[0]
            mais_similar_2 = self.artigos_similares[1]

            text = f'Artigos mais similares: \n'
            text += f'{mais_similar_1} \n'
            text += f'{mais_similar_2} \n'
        return text