#DEBUG

#elif / else = sempre depende do if, else sempre e o ultimo a ser executado

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1: #IF sempre e true
    print('codigo para condicao 1')#Dentro do bloco
elif condicao2:
    print('CODIGO 2')
elif condicao3:
    print('CODIGO 3')
elif condicao4:
    print('CODIGO 4')
else:                           #Se nenhuma condicao for true, essa vai rodar 
    print('CODIGO ESTA FORA')

#quando encontrar uma condicao verdadeiro ele vai retornar ele e vai pular as outras


print('fora do if')#esta fora do bloco

if 10 == 10:
    print('Outro if')#pode ter outro if independente