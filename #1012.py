#1012
# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))
tri = A * C / 2
cir = 3.141559 * (C * C)
tra = (A + B) * C / 2
qua = B * B
ret = A * B
print(f'Triangulo: {tri}\nCirculo: {cir}\nTrapezio: {tra}\nQuadrado: {qua}\nRetangulo: {ret}')