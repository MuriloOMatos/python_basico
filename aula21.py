#Operador logico
#And(e) or(ou) not(nao)
#And - todas as condicoes precisam ser verdadeiras
#se qualquer valor for considerado falso,
#a expressao inteira sera avaliada n aquele valor
# Sao considerados falsy = 0 / 0.0 / "" / false
#Tambem existe o tipo none que e usado para representar um nao valor

entrada = input('[E]NTRA [S]AIDA: ')
senha_digitada = input('Senha:  ')

senha_permitida = '123'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('ENTRAR')

else:
    print('SAIR')

#Avalicao de curto circuito 
#Para economizar quando o sistema ve que uma expressao e falsa ele ja para nela porque o resto ira rotorna FALSE 
print(True and False and True) 
print(True and 0 and True)