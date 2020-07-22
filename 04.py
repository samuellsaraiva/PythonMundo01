'''Aula 08 Mundo 01 // Utilizando Módulos'''



'''
bebida = [suco, refri, cerveja, vodka]
comida = [caramão, estrogonofe, lasanha]
doce = [beijinho, brigadeiro, balinha, chiclete]

import bebida #importar todos os valores de bebida
from bebida import suco #importar somente o "suco" de bebida


exemplo de uma biblioteca:
import math
funcao ceil vai arredondar pra cima
funcao floor vai arredondar pra baixo
funcao trunc vai eliminar o valor da virgula pra frente
funcao pow vai funcionar como potenciacao
funcao sqrt vai calcular a raiz quadrada
funcao factorial vai calcular o fatorial de um numero
'''

# import math
# num = int(input('Informe o Nº: '))
# raiz = math.sqrt(num)
# print(f'A raíz de {num} é igual a {raiz}')
# print(f'Arredondado para cima: {math.ceil(raiz)}')
# print(f'Arredondado para baixo: {math.floor(raiz)}')
# print(f'Inteiro, ou seja, sem virgula: {math.trunc(raiz)}')
# print(f'Fatorial dessa raiz: {math.factorial(raiz)}')
# print(f'A raíz de {num} é igual a {raiz:.2f}') #neste caso, vai arredondar com duas casas decimais


# from math import sqrt, ceil
# num = int(input('Informe o Nº: '))
# #raiz = math.sqrt(num) #não é necessário o "math.", pois ja foi importado especificamente, logo ficará:
# raiz = sqrt(num)
# print(f'A raíz de {num} é igual a {raiz}')
# #print(f'Arredondado para cima: {math.ceil(raiz)}') #mesma coisa neste caso, logo ficará:
# print(f'Arredondado para cima: {ceil(raiz)}')

# from math import sqrt as raizquadrada  # "as" informa que vai ser importado de acordo com a variavel respectivamente informada, neste caso "raiz quadrada"
# num = int(input('Informe o Nº: '))
#raiz = raizquadrada(num) # logo, "sqrt" é igual a "raizquadrada"


# import random
# num = random.random() #importa algum numero aleatorio de 0 até 1
#num = random.uniform(0,10) #importa algum numero aleatorio de X até Y sendo float
# num1 = random.randint(1, 10) #importa algum numero INTEIRO aleatorio de 1 até 10
# print(num)
# print(num1)

# import emoji
# print(emoji.emojize('Olá mundo, :sunglasses:', use_aliases=True)) #para verificar mais detalhes de 'emojis' é necessário verificar o PYPI dessa biblioteca





'''
desafio 16
- ler um numero real qualquer pelo teclado e mostre na tela sua porção inteira
'''
# import random
# import math
# num = random.uniform(1,10)
# inteiro = math.trunc(num)
# print(f'Numero decimal: {num}')
# print(f'Numero inteiro: {inteiro}')


'''
desafio 17
- ler o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
'''
# catop = int(input('Informe o valor do cateto oposto: '))
# catad = int(input('Informe o valor do cateto adjacente: '))
# hip = ((catop)**2 + (catad)**2 )**(1/2)
# print(f'Valor da hipotenusa: {hip:.2f}')


'''
desafio 18
- ler um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
'''
# import math
# ang = float(input('Informe o valor do angulo: '))
# seno = math.sin(ang)
# cosseno = math.cos(ang)
# tangente = math.tan(ang)
# print(f'\nValor do Seno do ângulo de {ang}º é: {seno:.2f}\n'
#       f'Valor do Cosseno do ângulo de {ang}º é: {cosseno:.2f}\n'
#       f'Valor da Tangente do ângulo de {ang}º é: {tangente:.2f}')


'''
desafio 19
- sortear um dos 4 nomes informados e diga o nome do escolhido
'''
# import random
# listanomes = ['samuel', 'julia', 'hericlys', 'isabella']
# sortear = random.choice(listanomes)
# print(sortear)


'''
desafio 20
- sortear uma ordem específica e ler os nomes mostrando a ordem sorteada
'''
# import random
# listanomes = ['samuel', 'julia', 'hericlys', 'isabella']
# random.shuffle(listanomes)
# print(f'Novas posições: {listanomes}')


'''
desafio 21
- faça um programa que abra e reproduza algum audio de arquivo mp3 // **desnecessário**
'''
# import pygame
# pygame.init()
# pygame.mixer.music.load('04.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()