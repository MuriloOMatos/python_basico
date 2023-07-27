a = 'A' #0
b = 'B' #1
c = 1.1 #2
 
#A ordem da chave determina quem vem primeiro, sendo sempre o primeiro da direita para esquerda
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b ,c) #dentro do indice as variaves sao numeradas sendo o primeiro o 0
print(formato) 

#Numerando as string podemos invetermos a ordem de chamada nao dependendo de saber qual e a primeira chave
#Numeração sempre começa no 0

string = 'b={1} a={0} c={2:.2f}'
formato = string.format(a, b ,c)
print(formato)

#Parametro nomeado

string = 'b={nome2} a={nome1} c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b ,nome3=c)
print(formato)