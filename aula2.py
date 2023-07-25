# \r\n => CRLF, Que significa a quebra da linha pode ser utilizado somente o \n

#carecteres nao nomeados 
print(1,2,3,)

#caracteres nomeado sao os espacos entre os numeros, podendo ser nomeados com o comando sep=()
print(1,2,3, sep='-')


#pode ser nomeado tambem a quebra da linha, que por padrao ja vem \r\n podendo ser editada pelo comando end=()

#sem quebra de linha
print(1,2,3, sep='-',end=('.'))
print(1,2,3,)

#quebra de linha
print(1,2,3, sep='-',end=('.\n'))
print(1,2,3,)