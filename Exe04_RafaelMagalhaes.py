#No SenaiLandia mulheres e homens podem servir o exercito do pais. O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida.
#Existem uma única restrição para o ingresso que é a idade da pessoa:
#--- Para mulheres a idade aceita é entre 21 e 34 anos
#--- Para homens a idade aceita é entre 18 e 39 anos.

#Escreva um programa que leia três dados de entrada: Nome, idade e sexo, e informe se a pessoa será aceita ou não para o serviço.
#OBS: Para o sexo deve ser lido apenas um caractere que pode ser "f" ou "F", "m" ou "M" (m = masculino e f = feminino). Qualquer coisa diferente deve ser invalido

nome = (input("Digite seu nome: "))
idade = int (input("Digite sua idade: "))
sexo = (input("Digite seu sexo ('f' para femenino e 'm' para masculino): "))
sexo = sexo.lower()
nome = nome.title()

if sexo == "f" and idade > 21 and idade <34: #Ok
    print("{}, você foi aceita para servir o exercito!".format(nome))

elif sexo == "m" and idade > 18 and idade <39: #OK
    print("{}, você foi aceito para servir o exercito!".format(nome))

elif sexo != 'm' and sexo != 'f':
        print("Sexo invalido,você não foi aceito")

 
elif sexo == 'm' and idade <18:
    print("Idade invalida,você não foi aceito/a")

elif sexo == 'f' and idade <21:
    print("Idade invalida,você não foi aceito/a")

