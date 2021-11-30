import pandas as pd
import pandas_datareader.data as pdr
import datetime as dt
import json
import os

def carregar_preco_bitcoin(inicio=(2015,1,1), fim=None):
    '''
    Parâmetros:
        inicio (tupla): data de início para baixar os dados. Se não passado, será (2015, 1, 1).
            formato: (ano, mes, dia).
        fim (tupla): data de início para baixar os dados. Se não passado, será data do dia.
            formato: (ano, mes, dia).
    
    Retorno:
        bitcoin_df (dataframe): preços de bitcoin para os dias entre o intervalo inicial e final.
    '''
    
    ano_inicio, mes_inicio, dia_inicio = inicio
    data_inicial = dt.date(ano_inicio, mes_inicio, dia_inicio)
    
    if fim is None:
        data_final = dt.date.today()
    else:
        ano_fim, mes_fim, dia_fim = fim
        data_final = dt.date(ano_fim, mes_fim, dia_fim)
        
    bitcoin_df = pdr.DataReader('BTC-USD', 'yahoo', data_inicial, data_final)
    bitcoin_df.index = pd.to_datetime(bitcoin_df.index)
    
    return bitcoin_df

def filtrar_dataframe(input_df, colunas, intervalo_data):
    '''
    Parâmetros:
        input_df (dataframe): dataframe de entrada.
        colunas (str): nome das colunas que serão filtradas no dataframe, separadas por vírgula.
        intervalo_data (str): intervalo de datas que serão filtadas no dataframe.
            formato: aaaa-mm-dd:aaaa-mm-dd para intervalo ou aaaa-mm-dd para data única.
    
    Retorno:
        resposta (dataframe): dataframe filtrado.
    '''
        
    df = input_df.copy()
        
    if intervalo_data.lower() == 'all':
        resposta_linha = df
    else:
        resposta_linha = filtrar_dataframe_linhas(df, intervalo_data)
        
    if isinstance(resposta_linha, pd.DataFrame):
        if colunas.lower() == 'all':
            resposta = resposta_linha
        else:
            resposta = filtrar_dataframe_colunas(resposta_linha, colunas)
    else:
        resposta = resposta_linha
        
    return resposta
    
def filtrar_dataframe_linhas(input_df, intervalo_data):
    '''
    Parâmetros:
        input_df (dataframe): dataframe de entrada.
        intervalo_data (str): intervalo de datas que serão filtadas no dataframe.
            formato: aaaa-mm-dd:aaaa-mm-dd para intervalo ou aaaa-mm-dd para data única.
    
    Retorno:
        resposta (dataframe): dataframe filtrado por datas (linhas).
    '''
    df = input_df.copy()
    
    if len(intervalo_data) == 10:
        inicio = intervalo_data[:10]
        fim = intervalo_data[:10]
    elif len(intervalo_data) == 21:
        inicio = intervalo_data[:10]
        fim = intervalo_data[-10:]
        
    try:
        df_filtrado = df.loc[inicio:fim]
    except:
        resposta = 'Erro: Não foi possível filtrar os dados. Por favor, verifique os parâmetros para datas' 
    else:
        resposta = df_filtrado
    finally:
        return resposta

def filtrar_dataframe_colunas(input_df, colunas):
    '''
    Parâmetros:
        input_df (dataframe): dataframe de entrada.
        colunas (str): nome das colunas que serão filtradas no dataframe, separadas por vírgula.
    
    Retorno:
        resposta (dataframe): dataframe com colunas filtadas.
    '''
    
    df = input_df.copy()
    lista_colunas = colunas.split(',')
    lista_colunas = [coluna.strip().capitalize() for coluna in lista_colunas]
       
    try:
        df_filtrado = df.loc[:, lista_colunas]
    except:
        resposta = 'Erro: Não foi possível filtrar os dados. Por favor, verifique os parâmetros para colunas' 
    else:
        resposta = df_filtrado
    finally:
        return resposta
    
def formatar_resposta_json(input_resposta):
    '''
    Parâmetros:
        input_resposta (dataframe/str): dataframe ou string para ser transformado em json
    
    Retorno:
        resposta_json (json): resposta no formato json
    '''
    
    if isinstance(input_resposta, pd.DataFrame):
        resposta = input_resposta.copy()
        resposta.index = resposta.index.strftime('%Y-%m-%d')
        resposta = resposta.round(decimals=2)
        resposta_json = resposta.to_json()
    else:
        mensagem = '"mensagem":"{' + input_resposta + '}"'
        resposta_json = json.loads(mensagem)
        
    return resposta_json
    
def agregar_valores(input_df, parametros_agg = ['min', 'max', 'mean']):
    '''
    Parâmetros:
        input_df (dataframe): dataframe de entrada.
        parametros_agg (lista): parâmetros para agregação dos dados. Se não passado, será: ['min', 'max', 'mean'].
    
    Retorno:
        df_agg (dataframe): dataframe agrupados por mês e ano com os parâmetros para agregação.
    '''
    
    df = input_df.copy()
    df['Mes'] = df.index.month
    df['Ano'] = df.index.year
    df_agg = df.groupby(['Mes', 'Ano']).agg(parametros_agg)
    
    return df_agg

def salvar_agregado(input_df, caminho_arquivo):
    '''
    Parâmetros:
        input_df (dataframe): dataframe de entrada.
        caminho_arquivo (str): caminho completo e nome do arquivo.
    Retorno:
        arquivo .csv e .json com os dados agrupados salvos no diretório.
    '''
    
    df = input_df.copy()
    diretorio = os.path.dirname(caminho_arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    df.to_csv(f'{caminho_arquivo}.csv')
    df.to_json(f'{caminho_arquivo}.json')
