"""
Formatacao basica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal

(caractere)   (><^)   (quantidade)
exp:           $>10

> - Esqueda
< - Direita
^ - Centro
= - forca o numero a aparecer antes do zero

conversion flags - !r !s !a
"""

Variavel = 'ABC'
#PADDING
print(f'{Variavel}')
print(f'{Variavel:>10}')
print(f'{Variavel:<10}')
print(f'{Variavel:^10}')
print(f'{Variavel:!^10}')

print(f'{1000.12301231:,.1f}')
print(f'{1000.12301231:0=+10,.2f}')
print(f'o hexadecimal de 1500 e {1500:08X}')

#conversion flags
print(f'{Variavel!r}')