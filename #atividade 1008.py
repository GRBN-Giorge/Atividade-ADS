#atividade 1008
# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

nf = int(input('Insira o número de funcionário: '))
hr = int(input('Insira o número de horas trbalhadas: '))
val = float(input('Insira o valor recebido por hora: '))

print(f'NUMBER = {nf} \nSALARY = {hr*val}')