from time import sleep
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opcao = 0
while opcao != 5:
    print('''
    [1] somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa.''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Finalizando.....')
    else:
        print('Opção inválida. Tente Novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do Programa! Volte Sempre.')