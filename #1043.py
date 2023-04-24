#1043
# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

a = float(input('1º valor: '))
b = float(input('2º valor: '))
c = float(input('3º valor: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print(f'perímetro = {a+c+b}')
else:
    print(f'Area = {(a+b)*c/2}')