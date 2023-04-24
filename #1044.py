#1044
# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

n1 = int(input('Insira o primeiro valor: ')) 
n2 = int(input('Insira o segundo valor: ')) 
if n2 % n1 == 0: 
    print('São múltiplos') 
else: 
    print('Não são múltiplos')
