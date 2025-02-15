#Escreva um programa para exibir na tela o nome e a categoria de um lutador o programa deve ler um string para o nome e um número real para o peço. 
#Conforme o peso ocorrera o enquadramento na categoria.

nome = str (input("Digite seu nome: "))
peso = float (input("Digite seu peso em kg: "))

if peso  <52:
    print('{}, sua categoria é ivalida'.format(nome))

elif peso  >=52 and peso <65:
    print('{}, sua categoria é "Pena"'.format(nome))

elif peso  >=65 and peso <72:
    print('{}, sua categoria é "Leve"'.format(nome))

elif peso  >=72 and peso <79:
    print('{}, sua categoria é "Ligeiro"'.format(nome))

elif peso  >=79 and peso <86:
    print('{}, sua categoria é "Meio Médio"'.format(nome))

elif peso  >=86 and peso <90:
    print('{}, sua categoria é "Médio"'.format(nome))

elif peso  >=90 and peso <100:
    print('{}, sua categoria é "Meio pesado"'.format(nome))

elif peso  >= 100:
    print('{}, sua categoria é "Pesado"'.format(nome))
