# Operador logico "not"
# Usado para inverter expresoes
# not true = false
# not false = true

print(not True) #false
print(not False)#true


#SE a senha nao for digitada o if irar funcionar pq '' agr e true
senha = input('Senha: ')
if not senha:
    print('SENHA INCORRETA')