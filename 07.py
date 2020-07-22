'''Aula 11 Mundo 01 // Cores no terminal'''



'''
comando pricipal: \33[m
pode-se adicionar até "3" comandos entre o [ e o m
sendo o 1º do estilo, o 2º do texto e o 3º do background

exemplo: \333[0;33;44m

códigos para estilo: 0(sem estilo nenhum), 1(em negrito), 4(sublinhado) e 7(inverter as configurações)
códigos para texto: 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(roxo), 36(azul bb) e 37(cinza)
códigos para background: 40(branco), 41(vermelho), 42(verde), 43(amarelo), 44(azul), 45(roxo), 46(azul bb) e 47(cinza)
'''

print('\33[31mOlá, mundo!') #para escrever 'Olá, mundo!' em vermelho
print('\33[1;31mOlá, mundo!') #em negrito
print()


print('\33[31;43mOlá, mundo!') #para escrever 'Olá, mundo!' em vermelho e o fundo amarelo
print('\33[31;43mOlá, mundo!\33[m') #para escrever 'Olá, mundo!' em vermelho e o fundo amarelo e tirar a continuação do background pós termino da frase
print()


print('\33[1;31mOlá, mundo!\33[m') #em negrito sem background
print()


print('\33[4;30;45mOlá, mundo!\33[m') #sublinhado com letra branca e fundo roxo
print()


print('\33[35mOlá, mundo!\33[m') #letra branca fundo padrão
print('\33[35;7mOlá, mundo!\33[m') #inverte o ex de cima
print()
print()
print()


a = 5
b = 4
print(f'O valor de [a] é \33[32m{a}\33[m e o valor de [b] é \33[31m{b}\33[m')
print()
print()
print()


nome = 'samuel'
cores = {'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'branco':'\033[30m',
         'roxo':'\033[35m',
         'verde':'\033[32m',
         'ciano':'\033[36m',
         'limpa':'\033[m',
         'preto e branco':'\033[7;30;m',
         'vermelho em negrito':'\033[1;31m',
         'azul em negrito':'\033[1;34m' ,
         'amarelo em negrito':'\033[1;33m' ,
         'branco em negrito':'\033[1;30m',
         'roxo em negrito':'\033[1;35m',
         'verde em negrito':'\033[1;32m',
         'ciano em negrito':'\033[1;36m',
         'vermelho sublinhado':'\033[4;31m',
         'azul sublinhado':'\033[4;34m',
         'amarelo sublinhado':'\033[4;33m',
         'branco sublinhado':'\033[4;30m',
         'roxo sublinhado':'\033[4;35m',
         'verde sublinhado':'\033[4;32m',
         'ciano sublinhado':'\033[4;36m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelho'], nome, cores['limpa']))