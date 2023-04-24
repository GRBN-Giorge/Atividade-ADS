#1048
# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

sal = float(input('Insira seu salário: ')) 
sals = sal 
if sal <= 400.00: 
    sals *= 0.15 
    acrec = sal+sals 
    print(f'Novo salário: {acrec} \nReajuste ganho: {sals} \nPercentual: 15% ') 
elif sal >= 400.01 and sal <= 800.00: 
    sals *= 0.12 
    acrec = sal+sals 
    print(f'Novo salário: {acrec} \nReajuste ganho: {sals} \nPercentual: 12% ') 
elif sal >= 800.01 and sal <= 1200.00: 
    sals *= 0.10 
    acrec = sal + sals 
    print(f'Novo salário: {acrec} \nReajuste ganho: {sals} \nPercentual: 10% ') 
elif sal >= 1200.01 and sal <= 2000.00: 
    sals *= 0.07 
    acrec = sal + sals 
    print(f'Novo salário: {acrec} \nReajuste ganho: {sals} \nPercentual: 07% ') 
elif sal > 2000.00: 
    sals *= 0.04 
    acrec = sal + sals 
    print(f'Novo salário: {acrec} \nReajuste ganho: {sals} \nPercentual: 04% ') 