#Nas eleições municipais os municipios com 200.000 mil eleitores ou mais tem segundo turno caso o primeiro colocado não tenha mais que 50% dos votos. 
# Escreva um programa que leia o nome do municipio, a quantidade de eleitores a quantidade de votos do canditado mais votado e informe se havera segundo turno.

municipio = (input("Digite o nome do municipio: "))

eleitores = (input("Digite a quantidade de eleitores: "))

votos = (input("Digite a quantidade de votos do canditado mais votado: "))

turno2 = eleitores/2

if eleitores >= 200000 and turno2 < votos:
    