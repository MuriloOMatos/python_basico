primeiro_valor = input('Inserir Valor:')
segundo_valor = input('Inserir segundo valor:')

intvalor = int(primeiro_valor)
intvalor2 = int(segundo_valor)

maior_que = intvalor > intvalor2

if maior_que:
    print(f'PRIMEIRO VALOR  "{primeiro_valor}" e maior que o segundo valor  "{segundo_valor}"')

else:
    print(f'SEGUNDO VALOR  "{segundo_valor}" e maior que o primeiro valor "{primeiro_valor}"')