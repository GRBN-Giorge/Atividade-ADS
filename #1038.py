#1038
if __name__ == '__main__':
    v = input('Digite o codigo do item e a quantidade separado por espaço: ').split()
    c, q = int(v[0]), int(v[1])

    c1 = float(4.00)
    c2 = float(4.50)
    c3 = float(5.00)
    c4 = float(2.00)
    c5 = float(1.50)

    if c == 1:
        t = q * c1
    elif c == 2:
        t = q * c2
    elif c == 3:
        t = q * c3
    elif c == 4:
        t = q * c4
    elif c == 5:
        t = q * c5
    else:
        print('Opção inválida, Digite um codigo valido')

    print('Total a pagar: R$ {:.2F} '.format(t))
