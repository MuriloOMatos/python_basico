'''F-STRING'''

nome = 'murilo matos'
altura = 1.67
peso = 80
imc = peso / (altura * altura)

Linha = f'{nome} tem {altura} de altura pesa {peso} quilos e seu imc e {imc:.2f}'

print(Linha)