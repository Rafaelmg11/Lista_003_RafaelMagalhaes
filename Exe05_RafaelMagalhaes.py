# No comercio o conceito de margem bruta é uma % que é aplicada ao preço de custo, para se obter o preço de venda. 
# Uma loja tem como politica comercial aplicar uma margem bruta de 45% quando o preço de custo é <=100 reais, se o produto custa mais que isso a margem bruta é de 35%.
#  Escreva um programa que leia o preço de custo do produto , e mostre na tela qual o seu preço de venda com duas casas decimais

produto = str (input("Digite qual é o produto: "))
valor = float (input("Digite qual é o valor do produto: "))

if valor <= 100:
    margem = valor + (valor * 0.45)
    print(" preço de venda de {}, é de R${}".format(produto,margem))
else:
    margem = valor + (valor * 0.35)
    print("O preço de venda de {}, é de R${}".format(produto,margem))

print("FIM DO CODIGO --- Rafael de Almeida de Magalhães")