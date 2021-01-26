from datetime import date
sexo = int(input("""Informe o seu sexo: 
[ 1 ] Masculino
[ 2 ] Feminino
Opção: """))
if sexo == 1:
    atual = date.today().year
    nasc = int(input('Digite o ano de seu nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {}, tem {} anos, em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você deve se alistar este ano.')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para seu alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter ser alistado ha {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento seria em {}'.format(ano))
elif sexo ==2:
    print('Voce não precisa se alistar.')



