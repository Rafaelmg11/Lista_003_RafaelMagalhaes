# Uma empresa financeira consegue empréstimos ás pessoas físicas, quando o valor da parcela é menor que 8% do salario da pessoa.
# Escreva um programa que leia dois números reais, o valor do salario e o valor da parcela e informe se o empréstimo será concedido ou não. 

salario = float (input("Digite qual é o valor do seu salario: "))
parcela = float(input("Digite qual é o valor da parcela: "))

emprestimo = salario * 0.08

if emprestimo < parcela:
    print("Empréstimo concedido!")
else:
    print("Emprestimo negado!")

print("FIM DO CODIGO --- Rafael de Almeida de Magalhães")