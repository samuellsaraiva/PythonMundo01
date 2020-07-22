'''Aula 07 Mundo 01 // Operadores aritméticos'''



'''
procedimentos que podem ser feitos através de caracteres em um print:
nome=str(input('Digite seu nome: '))
print(f'Prazer em te conhecer, {nome}!!')

nome=str(input('Digite seu nome: '))
print(f'Prazer em te conhecer, {nome:20}!!')   #o ":20" faz com que o campo em {} tenha 20 caracteres

nome=str(input('Digite seu nome: '))
print(f'Prazer em te conhecer, {nome:>20}!!')  #o ">" faz com que o nome fique para o lado direito

nome=str(input('Digite seu nome: '))
print(f'Prazer em te conhecer, {nome:<20}!!')  #o "<" faz com que o nome fique para o lado esquerdo

nome=str(input('Digite seu nome: '))
print(f'Prazer em te conhecer, {nome:^20}!!')  #o "^" faz com que o nome fique centralizado

nome=str(input('Digite seu nome: '))
print(f'Prazer em te conhecer, {nome:-^20}!!') #o "-" faz com que seja preenchido todos os outros caracteres restantes; vale para qualquer sinal indicado
'''



'''
#operadores aritméticos

adicao: +
subtracao: -
multiplicacao: *
divisao: /
potencia: **          ou pode-se utilizar o "pow"; ex: pow(4,3), ou seja, 4 elevado a 3. mesma coisa que 4**3
divisao inteira: //   #é o valor da divisão antes da vírgula
resto da divisao: %   #é o resto da divisão
raiz quadrada: x**(1/2)

#dá para multiplicar strings: oi*5 vai aparecer o "oi" 5x atraves do print
'''



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