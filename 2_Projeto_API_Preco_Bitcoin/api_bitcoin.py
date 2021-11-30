from flask import Flask, request, Response
from flask_restful import Resource, Api
import pandas as pd
import preco_bitcoin as pbit
from plotar_grafico import plotar_candlestick

app = Flask(__name__)
api = Api(app)

preco_bitcoin = pbit.carregar_preco_bitcoin()

class PrecoBitcoin(Resource):
    def get(self, colunas, data):
        df_preco = pbit.filtrar_dataframe(preco_bitcoin, colunas, data)
        resposta_json = pbit.formatar_resposta_json(df_preco)
        
        if isinstance(df_preco, pd.DataFrame):
            df_agregado = pbit.agregar_valores(df_preco)
            pbit.salvar_agregado(df_agregado, 'resultados/dados_agrupados')
            
            df_filtrado = pbit.filtrar_dataframe(preco_bitcoin, 'all', data)
            plotar_candlestick(df_filtrado, 'resultados/candlestick',
                              'Gráfico Candlestick Preço Bitcoin')

        return Response(resposta_json, mimetype='application/json')
    
api.add_resource(PrecoBitcoin, '/<string:colunas>/<string:data>')

if __name__ == '__main__':
    app.run(debug=True)
