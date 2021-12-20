import pandas as pd
import time 

#abre o arquivo e importa a lista
df = pd.read_csv('learning.csv\\project03\\dados.csv', encoding='ansi')

#mostra os dados que temos na lista
print('Confira os detalhes do arquivo...\n')
time.sleep(1)
print(df.head())
time.sleep(1)

#qual linha você deseja editar?
editRow = int(input("\nQual linha você deseja editar?\n\nDigite o número de 0 a {}: ".format(str(len(df) - 1))))
