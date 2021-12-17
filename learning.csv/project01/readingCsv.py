import csv
import time

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
                        time.sleep(0.1)
                        # nome, sexo, endereco, cidade, email, telefone, idade = data[x].split(',')
                        # print(nome)
                        myList=','.join([str(item) for item in data[x]])
                        myList.split(',')
                        print(myList[1])
                        # print('Nome: {}\nSexo: {}\nEndereço: {}\nCidade: {}\nE-mail: {}\nTelefone: {}\nIdade: {}'.format(myList[0], myList[1], myList[2], myList[3], myList[4], myList[5], myList[6]))
else:
        print("\nNome não encontrado, tente novamente.")