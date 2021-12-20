import csv 

#cria o nosso novo arquivo
with open ('.\\learning.csv\project02\dados.csv', 'w+', newline='', encoding='ansi') as fileOpened:
        myFile = csv.writer(fileOpened)
        myFile.writerow(["Nome", "Sexo", "Endereço", "Cidade", "E-mail", "Telefone", "Idade"])
        loop = int(input("Quantas pessoas você vai cadastrar? "))
        for i in range(loop):
            print("\nPreencha com os dados para finalizar o cadastro...\n")
            nome = input("\nPessoa {} - Nome: ".format(i+1))
            sexo = input("Pessoa {} - Sexo (M ou F): ".format(i+1))
            endereco = input("Pessoa {} - Endereço: ".format(i+1))
            cidade = input("Pessoa {} - Cidade: ".format(i+1))
            email = input("Pessoa {} - E-mail: ".format(i+1))
            telefone = input("Pessoa {} - Telefone: ".format(i+1))
            idade = input("Pessoa {} - Idade: ".format(i+1))
            myFile.writerow([nome, sexo, endereco, cidade, email, telefone, idade])
        
        