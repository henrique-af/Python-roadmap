import csv
import sys

#local do arquivo
filePath = '.\\learning.csv\project01\\arquivoDados.csv'

#realiza leitura do csv
data = []
with open (filePath, encoding='utf8') as fileOpened:
        reader = csv.reader(fileOpened, delimiter=',')
        for row in reader:
                data.append(row)
                
#qual nome deseja buscar?
nomeBusca = input('Digite o nome que deseja encontrar: ')

#realiza a leitura da coluna 0, que são os nomes e armazena em data
nomeColuna = [x[0] for x in data]

# busca o nome na coluna nome
if nomeBusca in nomeColuna:
        for x in range(0, len(data)):
                if nomeBusca == data[x][0]:
                        # nome, sexo, endereco, cidade, email, telefone, idade = data[x].split(',')
                        # print(nome)
                        myList = [data.split(',', 1)[0] for i in data]
                        print(myList)
else:
        print("\nNome não encontrado, tente novamente.")
        
# reader = list(csv.reader(open(, encoding='utf8'), delimiter=','))

# for [nome, sexo, endereco, cidade, email, telefone, idade] in reader:
#         i = 0;
#         if nome == nome.reader[i]:
#                 print('{} - {} - {} - {} - {} - {} - {}'.format(nome, sexo, endereco, cidade, email, telefone, idade))
#         else:
#                 i = i + 1;
        
        