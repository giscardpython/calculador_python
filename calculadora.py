
while True:
    # entrada de dados
    numero1 = str(input('Informe o 1o número: ')).replace(',','.')
    numero2 = str(input('Informe o 2o número: ')).replace(',','.')

    numero1 = float(numero1)
    numero2 = float(numero2)

    print('\nInforme a operação que desejas fazer:')
    print('"+"  para somar')
    print('"-"  para subtrair')
    print('"*"  para multiplicar')
    print('"/"  para dividir')
    print('"%"  para encontrar o resto da divisão')
    print('"x"  para encerrar o programa')
    
    op = input('Operação desejada: ')

    match op:
        case '+':
            print(f'A soma é: {numero1 + numero2}.')
        case '-':
            print(f'A subtração é: {numero1 - numero2}.')
        case '*':
            print(f'A multiplicação é: {numero1 * numero2}.')    
        case '/':
            print(f'A divisão é: {numero1 / numero2}.')    
        case '%':
            print(f'O resto da divisão é: {numero1 % numero2}.')
        case _:
            print('Operação inválida')
            continue                
        case 'x':
            break                
 