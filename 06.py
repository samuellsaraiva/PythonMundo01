'''Aula 10 Mundo 01 // Condições'''



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