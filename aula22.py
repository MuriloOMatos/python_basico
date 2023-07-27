#Operador logico
#And(e) or(ou) not(nao)
#Or - Qualquer condicao verdadeira avalia
#toda a expressao como verdadeira.
#Se qualquer valor for considerado verdadeiro,
#a expressao inteira sera avaliada naquele valor.


entrada = input('[E]NTRA [S]AIDA: ')
senha_digitada = input('Senha:  ')

senha_permitida = '123'

#Colchetes serve para organizar a linha que ficara ambígua
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('ENTRAR')

else:
    print('SAIR')


#Avaliacao por curto circuito

print(False or True or '')#Chegou no true, ja ira retornar true sem verificar a proxima considecao