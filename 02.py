'''Aula 06 Mundo 01 // Tipos primitivos e saídas de dados'''



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
t = input('Valor: ')
print(f'tipo primitivo: {type(t)}') #verificar qual o tipo do valor informado: str, int, float, etc
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
n = input('Digite o valor: ')
print(n.isalnum()) #se é alfanumerico (letra + numero - "3a")

print(n.isdecimal()) #se é número decimal

print(n.isnumeric()) #se é número

print(n.isalpha()) #se é letra

print(n.isascii()) #It is a numeric value given to different characters and symbols, for computers to store and manipulate. ex: letter 'A' is 65.

print(n.isdigit()) #se a string é composta apenas por números // isdigit() checks whether the string consists of digits only.

print(n.isidentifier()) #A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
                        #A valid identifier cannot start with a number, or contain any spaces.

print(n.isprintable()) #se pode ser impresso / mostrado

print(n.isspace()) #se é um "espaço", ou seja, se é um caracter "em branco"

print(n.istitle()) #se está capitulada, ou seja, se tem maiúscula na primeira letra e o resto minúscula na mesma palavra

print(n.islower()) #se está somente com letras minúsculas

print(n.isupper()) #se está somente com letras maiúsculas
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

'''
desafio 04
- ler algo pelo teclado e mostra na tela seu tipo primitivo e todas as informações sobre ele
'''
# v = input('Valor desejado: ')
# print(f'tipo primitivo: {type(v)}')
# print(n.isalnum())
# print(n.isdecimal())
# print(n.isnumeric())
# print(n.isalpha())
# print(n.isascii())
# print(n.isdigit())
# print(n.isidentifier())
# print(n.isprintable())
# print(n.isspace())
# print(n.istitle())
# print(n.islower())
# print(n.isupper())