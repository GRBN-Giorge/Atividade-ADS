#1051
sal = float(input('Digite seu salário: ')) 
if sal <= 2000: 
    print('Isento de impostos') 
elif sal >= 2000.01 and sal <= 3000: 
    print(f'O imposto a ser pago é e R$ {sal*0.08}') 
elif sal >= 3000.01 and sal < 4500: 
    print(f'O imposto a ser pago é de R$ {sal*0.18}') 
elif sal > 4500: 
    print(f'O imposto a se pago é de R$ {sal*0.28}') 