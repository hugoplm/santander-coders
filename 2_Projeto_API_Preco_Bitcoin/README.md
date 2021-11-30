# Projeto API Preços Bitcoin

Projeto elaborado para o segundo módulo do curso de Data Science da Let's Code.

O objetivo do projeto é criar uma API para filtrar dados de uma base aberta e 
retornar os dados filtrados por meio do método GET no formato JSON. 
Além disso, os dados filtrados deverão ser agrupados e salvos em formato CSV e JSON.
Por fim, deverá ser salvo um gráfico gerado a partir dos dados filtrados.

Para esse projeto, foi selecionado uma base de dados de preços de bitcoin, com
início a partir de 1 de Janeiro de 2015. Os dados podem ser adquiridos a partir
de uma API do Yahoo utilizando a biblioteca pandas-datareader e foram 
manipulados utilizando a biblioteca Pandas. A API foi criada utilizando 
a biblioteca Flask. O gráfico selecionado foi o de Candlestick, criado
utilizando a biblioteca Plotly.

Para executar a API, rodar o script "api_bitcoin.py".

**Parâmetros para método GET:**

/colunas/intervalo de data

colunas: nome das colunas que serão filtradas no dataframe. As colunas disponíveis no
dataframe original são: High, Low, Open, Close, Adj Close, Volume.

Observação: caso desejado selecionar todas as colunas, poderá ser utilizado o valor 'all'

intervalo de data: intervalo de datas que serão filtadas no dataframe. Dados disponíveis
de 1 de Janeiro de 2015 até a data de hoje (última validação em 29 de Novembro de 2021).

Os dados deverão ser passados nos seguintes formatos:
- para data uníca: aaaa-mm-dd
- para intervalo de data: aaaa-mm-dd:aaaa-mm-dd

Observação: caso desejado selecionar todas as datas disponíveis, poderá ser utilizado o valor 'all'

**Exemplos de chamada:**

1 - selecionar coluna 'High' e data de 29 de Novembro de 2021:

/high/2021-11-29

2 - selecionar colunas 'High', 'Low' e 'Volume' e data de 29 de Novembro de 2021:

/high,low,volume/2021-11-29

3 - selecionar coluna 'High' e intervalo de data de 01 de Novembro de 2021 à 29 de Novembro de 2021:

/high/2021-11-01:2021-11-29

4 - selecionar colunas 'High', 'Low' e 'Volume' e intervalo de data de 01 de Novembro de 2021 à 
29 de Novembro de 2021:

/high,low,volume/2021-11-01:2021-11-29

5 - selecionar todas as colunas e intervalo de data de 01 de Novembro de 2021 à 
29 de Novembro de 2021:

/all/2021-11-01:2021-11-29

6 - selecionar colunas 'High', 'Low' e 'Volume' e intervalo com todas as datas disponíveis:

/high,low,volume/all

7 - selecionar todas as colunas e e intervalo com todas as datas disponíveis:

/all/all

**Resultados:**

Na pasta 'resultados' pode ser visto o resultado da execução do exemplo 4 (colunas 'High', 'Low' e 'Volume' 
e intervalo de data de 01 de Novembro de 2021 à 29 de Novembro de 2021):

- arquivos CSV e JSON com os dados filtrados e agrupados por meses e anos.
- arquivo PNG com gráfico de candlestick.
