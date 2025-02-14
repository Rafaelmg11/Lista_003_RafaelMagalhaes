# 1 - Escreva um programa que forneça o tipo de aplicação financeira adequado a um investidor, a partir de dois dados fornecidos:
#  o grau de aceitação de risco e o valor a ser investido.
# O grau de aceitação de risco deve ser lido no teclado na forma 'BX' para baixo, ou , 'AL' para alto, se for fornecido algo diferente disso o programa deve mostrar um mensagem 
# indicando que foi fornecido dado invalido. Para o valor deve ser um numero real.

risco = str (input("Digite o grau de aceitação de risco que você deseja (BX para baixo, AL para alto): "))
risco = risco.lower
valor = float (input("Digite o valor a ser investido: "))

#Investimento Baixo:
if risco == "bx" and valor <1000:
    print("Invista na poupança")
elif risco == "bx" and valor >=1000:
    print("Invista na Renda Fixa")

#Investimento Alto:
elif risco == "al" and valor <1000:
    print("Invista em Bitcoins")
elif risco == "al" and valor >=1000:
    print("Invista em Ações")




