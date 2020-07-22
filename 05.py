'''Aula 09 Mundo 01 // Manipulando Textos'''



'''
#fatiamento
frase = 'curso em video python'
print(frase[9]) #vai mostrar o nono caracter
print(frase[9:13]) #vai mostrar do nono caracter ao décimo terceiro
print(frase[9:20:2]) #vai mostrar do nono caracter ao vigésimo pulando de 2 em 2
print(frase[:5]) #vai mostrar desde o início até o 5 caracter
print(frase[15:]) #vai mostrar tudo em diante a partir do 15º caracter
print(frase[4::2]) #vai mostrar tudo do quarto caracter em diante pulando de 2 em 2
backward = frase[::-1] #ler a frase de trás para frente
'''


'''
#Análise
frase = 'curso em video python'
print(len(frase)) #mostra o tamanho da frase
print(frase.count('o')) #vai contar quantas vezes aparece o caracter 'o' na frase toda
print(frase.count('o', 0, 13)) #vai fazer o mesmo que o ex de cima, porém dessa vez vai mostrar somente entre a posição 0 e a 13
print(frase.find('deo')) #vai dizer o "momento"/posição em que começou o caracter 'deo'
print(frase.find('android')) #se informar alguma string que nao contenha na frase, irá retornar "-1" indicando que não existe
print('curso' in frase) #vai mostrar se existe ou não o caracter desejado, neste caso 'curso', informando True ou False
'''



'''
#Transformação
frase = 'Curso em Video Python'
print(frase.replace('python', 'android')) #vai trocar a string 'python' pela string 'android'
print(frase.upper()) #vai deixar todos os caracteres em maiusculo
print(frase.lower()) #vai deixar todos os caracteres em minusculo
print(frase.capitalize()) #vai jogar todos os caracteres para minusculo e somente o primeiro vai ficar em maiusculo
print(frase.title()) #vai analisar quantas palavras tem na 'frase' a partir dos "espaços" e transformar todas os 1ºs caracteres das palavras em maiusculo
frase1 = '   Aprenda Python   '
print(frase1)
print(frase1.strip()) #vai remover todos os caracteres "inuteis" no inicio e no final da string
print(frase1.rstrip()) #vai remover todos os caracteres "inuteis" ao final da string // "r" de right/direita
print(frase1.lstrip()) #vai remover todos os caracteres "inuteis" no inicio da string // "l" de left/esquerda
'''



'''
#Divisão
frase = 'Curso em Video Python'
print(frase.split()) #vai mostrar todos os caracteres da frase em tuplas separadas, considerando os espaços, recomeçando a posição/indices de cada tupla
                     #a palavra Curso é 1, a palavra em é 2, a palavra Video é 3 e a palavra Python é 4
                     #vai dividir a string em uma lista, onde cada elemento vai ser separado pelo "espaço"
dividido = frase.split()
print(dividido[0]) #vai mostrar a primeira tupla formada, neste caso, 'Curso' 
'''



'''
#Junção
frase = 'Curso em Video Python'
print('-'.join(frase)) #vai espaçar todos os caracteres com o simbolo informado, neste caso '-'
print(frase.join('--')) #vai adicionar no inicio da string e no final da string o simbolo informado
print(frase.join('----')) #vai recriar a string para colocar os demais caracteres restantes -1
print(frase.join('\n'*11)) #vai recriar a string multiplicando ela por 11 menos 1, ou seja, vai mostrar a string 10x
'''



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