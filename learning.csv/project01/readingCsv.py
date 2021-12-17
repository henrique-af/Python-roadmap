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
while True:            
#qual nome deseja buscar?
        nomeBusca = input('\nDigite o nome que deseja encontrar ou 0 para parar: ')
        
#condição de parada do loop
        if nomeBusca == '0':
                break 
             
#realiza a leitura da coluna 0, que são os nomes e armazena em data
        nomeColuna = [x[0] for x in data]
                 
# busca o nome na coluna nome
        if nomeBusca in nomeColuna:
                for x in range(0, len(data)):
                        if nomeBusca == data[x][0]:
                                time.sleep(0.6)
                                myList=','.join([str(item) for item in data[x]])
                                myList_ = myList.split(',')
                                print('\nNome: {}\nSexo: {}\nEndereço: {}\nCidade: {}\nE-mail: {}\nTelefone: {}\nIdade: {}'.format(myList_[0], myList_[1], myList_[2], myList_[3], myList_[4], myList_[5], myList_[6])) 
        else:
                        print("\nNome não encontrado, tente novamente.")