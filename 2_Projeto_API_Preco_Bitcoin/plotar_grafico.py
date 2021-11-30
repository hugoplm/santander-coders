import plotly.graph_objs as go
import os

def plotar_candlestick(input_df, caminho_arquivo, titulo_grafico):
    '''
    Parâmetros:
        input_df (dataframe): dataframe de entrada.
        caminho_arquivo (str): caminho completo e nome do arquivo.
        titulo_grafico (str): título do gráfico para impressão.
    Retorno:
        arquivo .png com o gráfico de candlestick para o período selecionado salvo no diretório.
    '''
    
    data = [go.Candlestick(x=input_df.index,
                           open=input_df.Open,
                           high=input_df.High,
                           low=input_df.Low,
                           close=input_df.Close)]

    layout = go.Layout(title=titulo_grafico,
                      xaxis={'rangeslider':{'visible':False}})

    fig = go.Figure(data=data,layout=layout)
    
    diretorio = os.path.dirname(caminho_arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    fig.write_image(f'{caminho_arquivo}.png')
