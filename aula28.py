"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

Nome =input('INSERIR SEU NOME E SOBRENOME:  ')
Idade =input('INSERIR SUA IDADE:  ')

if Nome and Idade:
    print(f'seu nome {Nome} e sua Idade e {Idade}')
    print(f'Seu nome invertido é ({Nome[::-1]})')
    if ' ' in Nome:
        print('Seu nome (contém) espaços')
    else:
        print('Seu nome (não contém) espaços')
    print(f'Seu nome tem {len(Nome)} letras')
    print(f'A primeira letra do seu nome é ({Nome[0:1]})')
    print(f'A última letra do seu nome é ({Nome[-1:]})')

else:
    print('Desculpe, você deixou campos vazios.')