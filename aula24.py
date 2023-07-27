#operador in(esta entre) e not in(nao esta entre)
#string sao iteraveis
# 0 1 2 3 4 5
# m u r i l o
#-6-5-4-3-2-1
Nome = 'murilo'
'''print(Nome[2])
print(Nome[-3])'''

print('rilo' in Nome) #Confere se tem 'rilo' na variavel nome se tiver retorna true
print('zero' in Nome)

Nome = input('Digite nome')
encontrar = input('digite oq quer encontrar  ')

if encontrar in Nome:
    print(f'{encontrar} esta em {None}')

else:
    print(f'{encontrar} nao esta em {Nome}')