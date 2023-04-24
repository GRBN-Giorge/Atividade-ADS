#1015
# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

print('Calcular a distância.')
x1 = float(input('Insira x1: '))
y1 = float(input('Insira y1: '))
x2 = float(input('Insira x2: '))
y2 = float(input('Insira y2: '))

d1 = ((x2-x1)*2 + (y2-y1)*2) ** (1/2)

print(d1)