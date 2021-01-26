num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO.
[2] Converter para OCTAL.
[3] Comverter para HÉXADECIMAL.
''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('O número {} convertido para Binário é {}.'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para Octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para Héxadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Queira escolher uma Opção valida.')
print('Fim Programa.')