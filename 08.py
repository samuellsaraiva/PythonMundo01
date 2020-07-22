'''Todos os desafios do Mundo 01'''


'''
desafio 01
- ler o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com o valor digitado
'''
# nome = str(input('Nome: '))
# print(f'Boas vindas, {nome}')


'''
desafio 02
- ler o dia, mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada
'''
# dia = int(input('Dia: '))
# mes = int(input('Mês: '))
# ano = int(input('Ano: '))
# print(f'Data de Nascimento: {dia}/{mes}/{ano}')


'''
desafio 03
- ler dois numeros e a soma entre eles
'''
# num1 = int(input('Primeiro Nº: '))
# num2 = int(input('Segundo Nº: '))
# print(f'1º Número informado: {num1}\n'
#       f'2º Número informado: {num2}\n'
#       f'Soma dos dois Nºs informados: {num1 + num2}')


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

'''desafio 5
ler um numero inteiro e mostre o seu sucessor e seu antecessor'''
# num = int(input('qual o nº deseja? '))
# print(f'Sucessor: {num + 1}\n'
#       f'Num informado: {num}\n'
#       f'Antecessor: {num - 1}')


'''desafio 6
- ler um numero e mostre seu dobro, triplo e sua raiz quadrada'''
# num = int(input('Nº desejado: '))
# print(f'Nº informado: {num}\n'
#       f'Seu dobro: {num*2}\n'
#       f'Seu triplo: {num*3}\n'
#       f'Sua raiz quadrada: {num**(1/2)}')


'''desafio 7
- ler duas notas de um aluno, calcule e mostre sua média'''
# nota1 = int(input('Nota 1: '))
# nota2 = int(input('Nota 2: '))
# media = (nota1 + nota2)/2
# print(f'Média da Nota 1 [{nota1}] com a Nota 2 [{nota2}] é igual a {media}')


'''desafio 8
- ler um valor em metros e o exiba convertido em centímetros e milímetros'''
# valor = int(input('Valor: '))
# cent = valor * 100
# mili = valor * 1000
# print(f'Valor informado: {valor}\n'
#       f'Conversão em centímetros: {cent} cm\n'
#       f'Conversão em milímetros: {mili} mm')


'''desafio 9
- ler um numero inteiro qualquer e mostre a sua tabuada'''
# num = int(input('Nº desejado: '))
# print(f'Tabuada do número {num}')
# print('=-=-=-=-=-=-=-=')
# print(f'|{num} X 0 = {num*0:^5}|\n'
#       f'|{num} X 1 = {num*1:^5}|\n'
#       f'|{num} X 2 = {num*2:^5}|\n'
#       f'|{num} X 3 = {num*3:^5}|\n'
#       f'|{num} X 4 = {num*4:^5}|\n'
#       f'|{num} X 5 = {num*5:^5}|\n'
#       f'|{num} X 6 = {num*6:^5}|\n'
#       f'|{num} X 7 = {num*7:^5}|\n'
#       f'|{num} X 8 = {num*8:^5}|\n'
#       f'|{num} X 9 = {num*9:^5}|\n'
#       f'|{num} X 10 = {num*10:^4}|')
# print('=-=-=-=-=-=-=-=')


'''desafio 10
- ler quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar; valor dolar: 5,25'''
# valor = int(input('Valor na carteira: '))
# valordolar = 5.25
# conversao = print(f'Valor disponível da carteira em dolar: {valor//valordolar}') #utilizado o "//" para obter valores exatos da conversão


'''desafio 11
- ler a largura e a altura de uma parede e a quantidade de tinta que é necessária para pintá-la; cada L de tinta pinta uma área de 2m²'''
# largura = int(input('Largura da parede: '))
# altura = int(input('Altura da parede: '))
# areaparede = largura * altura
# litragem = areaparede / 2
# print(f'\nLargura da parede: {largura}m\n'
#       f'Altura da parede: {altura}m\n'
#       f'\nÁrea total da parede: {areaparede}m²\n'
#       f'Litragem necessária de tinta: {litragem}L')


'''desafio 12
- ler o preço de um produto e mostre seu novo preço com 5% de desconto'''
# preco = float(input('Valor do produto: '))
# novopreco = preco * 0.95
# print(f'Valor anterior: R${preco}\n'
#       f'Novo valor: R${novopreco}')


'''desafio 13
- ler o salário de um funcionário e mostre seu novo salário com 15% de aumento'''
# salarioantigo = float(input('Salário sem aumento: '))
# salarioatual = salarioantigo * 1.15
# print(f'Salário sem aumento: {salarioantigo}\n'
#       f'Salário com aumento: {salarioatual}')


'''desafio 14
- ler uma temperatura em graus celsius e transformar em fahrenheit'''
# tempcelsius = float(input('Informe a temperatura em Celsius: '))
# tempfahrenheit = (1.8 * tempcelsius) + 32
# print(f'Temperatura em Celsius: {tempcelsius}\n'
#       f'Temperatura em Fahrenheit: {tempfahrenheit}')


'''desafio 15
- ler quantos dias um carro foi alugado e quanto de quilometragem foi andada e informar o valor a ser pago pela utilização; R$60/dia e R$0,15 / por KM'''
# quantdia = int(input('Quantidade de dias: '))
# quantkm = int(input('Quantidade de KM rodado: '))
# valorfinal = (60*quantdia) + (quantkm * 0.15)
# print(f'Valor a ser pago: {valorfinal}')


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


'''
desafio 22
- ler o nome completo de uma pessoa e mostre: 1) o nome todo maiusculo, 
                                              2) o nome todo minusculo, 
                                              3) quantas letras ao todo sem considerar o espaço e 
                                              4) quantas letras tem o primeiro nome
'''
# nome = 'Samuel Saraiva Campos'

# upper = nome.upper()
# print(f'Nome todo maiúsculo: {upper}')

# lower = nome.lower()
# print(f'Nome todo minúsculo: {lower}')

# contadorespaco = nome.count(' ')
# print(f'Quantidade de espaços: {contadorespaco}')

# tamanho = len(nome) - contadorespaco
# print(f'Quantidade de caracteres do nome sem espaço: {tamanho}')

# divisaofrase = nome.split()
# print(f'Nome informado dividido: {divisaofrase}')

# tamanho1nome = len(divisaofrase[0])
# print(f'Tamanho do primeiro nome informado: {tamanho1nome} caracteres')



'''
desafio 23
- ler um numero de 0 a 9999 e mostre na tela cada um dos digitos sorteados separadamente, ex: 1897 - 1 = milhar, 8 = centena, 9 = dezena e 7 = unidade
'''
# import random
# num = random.randint(0, 9999)
# print(f'Número sorteado: {num}')
# uni = num // 1 % 10
# dez = num // 10 % 10
# cent = num // 100 % 10
# mil = num // 1000 % 10
# print(f'Unidade: {uni}')
# print(f'Dezena: {dez}')
# print(f'Centena: {cent}')
# print(f'Milhar: {mil}')



'''
desafio 24
- ler o nome de uma cidade e diga se ela começa ou não com o nome [santo]
'''
# nomecidade = str(input('Digite o nome da cidade: '))
# nomedividido = nomecidade.split()
# primeironome = nomedividido[0]
# nomesanto = primeironome.find('Santo')
# print(f'Nome informado: {nomecidade}')
# print(f'Nome informado dividido: {nomedividido}')
# print(f'Primeiro nome informado: {primeironome}')
# print(f'Primeiro nome informado tem [Santo] em sua composição? {nomesanto}')



'''
desafio 25
- ler o nome de uma pessoa e diga se ela tem "silva" no nome
'''
# nomepessoa = str(input('Informe o seu nome completo: '))
# nomesilva = nomepessoa.find('Silva')
# print(f'Nome informado: {nomepessoa}')
# print(f'Possui [Silva] em sua composição? {nomesilva}')
# print('Silva' in nomepessoa)



'''
desafio 26
- ler uma frase pelo teclado e mostre: 1) quantas vezes aparece a letra 'a'
                                       2) em que posição ela aparece pela primeira vez
                                       3) em que posição ela aparece da ultima vez 
'''
# frase = str(input('Informe alguma frase de seu interesse: '))

# letraA = frase.count('a')
# print(f'Quantidade de letras [a]: {letraA}')

# primeiroA = frase.find('a')
# print(f'Primeiro [a] aparece na {primeiroA + 1}ª posição')

# ultimoA = frase.rfind('a')
# print(f'Último [a] aparece na {ultimoA + 1}ª posição')



'''
desafio 27
- ler o nome completo de uma pessoa mostrando em seguida o 1 nome e o ultimo nome dessa pessoa separadamente, ex: 1 = samuel, ultimo = campos
'''
# nome = str(input('Digite seu nome completo: ')).strip()
# nomedividido = nome.split()
# print(f'Primeiro nome: {nomedividido[0]}')
# ultimonome = nomedividido[-1]
# print(f'Ultimo nome: {ultimonome}')


'''
desafio 28
- Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5, e peça 
  para o usuário tentar descobrir qual foi o número escolhido pelo computador.
  O programa deverá escrever na tela se o usuário acertou ou errou.
'''
# import random
# num = random.randint(0, 5)
# num1 = int(input('Informe um número: '))
# if num == num1:
#     print('Você acertou.')
#     print(f'Número sorteado: {num}')
# else:
#     print('Você errou.')
#     print(f'Número sorteado: {num}')



'''
desafio 29
- Ler a velocidade de um carro; se ultrapassou os 80km/h, mostre uma mensagem dizendo 
  que ele foi multado. A multa vai custar R$7 para cada Km acima do limite.
'''
# velocidade = int(input('Informe a velocidade do carro em km/h: '))
# if velocidade <= 80:
#     print('Veiculo com velocidade dentro do permitido')
# else:
#     calc1 = velocidade - 80
#     calc2 = calc1*7
#     print(f'O veículo estava {calc1}km/h acima do permitido (80km/h)')
#     print(f'Valor da multa: R${calc2 + 100}')



'''
desafio 30
- Ler um numero inteiro e mostre se ele é par ou impar.
'''
# num = int(input('Informe um número inteiro: '))
# if num %2 == 0 and num != 0:
#     print('Número par')
# elif num == 0:
#     print('Zero não é par e nem ímpar')
# else:
#     print('Número ímpar')


'''
desafio 31
- Escreva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem
  cobrando R$0,50 por KM para viagens até 200km e R$0,45 para viagens acima de 200km.
'''
# distancia = int(input('Qual a distância em KM? '))
# if distancia <= 200:
#     valor = distancia*0.5
#     print(f'Valor a ser pago: R${valor:.2f}')
# else:
#     valor = distancia*0.45
#     print(f'Valor a ser pago: R${valor:.2f}')


'''
desafio 32
- Ler um ano e informar se ele é bissexto ou não.
'''
# ano = int(input('Informe o ano para saber se é bissexto ou não: '))
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print(f'O ano {ano} é bissexto.')
# else:
#     print(f'O ano {ano} não é bissexto.')



'''
desafio 33
- Ler 3 numeros e mostre qual é o maior entre eles e qual é o menor.
'''
# num1 = int(input('Informe o 1º Número: '))
# num2 = int(input('Informe o 2º Número: '))
# num3 = int(input('Informe o 3º Número: '))
# if num1 == num2 and num3:
#     print('Os números informados são iguais')
# elif num1 > num2 and num1 > num3:
#     print(f'O primeiro número digitado [{num1}] é maior que os outros 2')
# elif num2 > num1 and num2 > num3:
#     print(f'O segundo número digitado [{num2}] é maior que os outros 2')
# elif num3 > num1 and num3 > num2:
#     print(f'O terceiro número digitado [{num3}] é maior que os outros 2')



'''
desafio 34
- Escreva um programa que pergunte o salário de uma pessoa e calcule o valor de seu aumento.
  Para salários superiores a R$1.250, 10% a mais; Para inferiores ou iguais, 15% a mais.
'''
# salario = int(input('Informe o salário: '))
# if salario > 1249:
#     novosalario = salario*1.10
#     print(f'Salário com aumento: R${novosalario:.2f}')
# else:
#     novosalario = salario*1.15
#     print(f'Salário com aumento: R${novosalario:.2f}')



'''
desafio 35
- Ler o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
# a = float(input('Coloque o valor de um lado: '))
# b = float(input('Coloque o valor de outro lado: '))
# c = float(input('Coloque o valor de outro lado: '))

# if abs(b-c) < a < b + c and abs(a-c) < b < a + c and abs(a-b) < c < a + b:
#     print(f'Os lados {a}, {b} e {c} podem formar triângulo.')
# else:
#     print(f'Os lados {a}, {b} e {c} não podem formar triângulo.')