dias = int(input('Digite a quantidade de dias de aluguel do veiculo:'))
km = float(input('Digite o total de quilometros rodados: '))
pago = (dias*60)+(km+0.15)
print('Se voce rodou {}km em {}dias de aluguel. voce deverá paga R$:{:.2f} a locadora.'.format(km, dias, pago))
