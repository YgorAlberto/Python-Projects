import math
import random
import pygame
import time
import datetime

    #======= MUNDO 01=========

# cores = {'azul':'\033[1;36m',
#          'verm':'\033[1;31m',
#          'limpa':'\033[m',
#          'amar':'\033[1;33m',
#          'br':'\033[1;30m',
#          'verd':'\033[1;32m'}

#GUANABARA
# nome = input ("qual seu nome?")
# idade = input ("qual sua idade?")
# peso = input ("qual seu peso?")
# print (nome, idade, peso)

# nome = input ('qual seu nome?')
# print ('Olá', nome,' seja bem vindo(a)')
#
# nome = input('qual seu nome?')
# dia = input('qual o dia de seu nascimento?')
# mes = input('qual o mes de seu nascimento?')
# ano = input('qual o ano do seu nascimento?')
#
# print (nome, 'Voce nasceu no dia', dia,'do mes', mes, 'do ano de', ano,', certo?')

# nasc = input ('qual sua data de nascimento')
# print (nasc)

# num1 = int(input('entre com o Numero 1'))
# num2 = int(input('entre com o Numero 2'))
# soma = (num1) + (num2)
# print (type (num1))
# print ('a soma entre {} e {} é: {}'.format(num1, num2, soma))
#
#     EXERCICIO 001
#
# print('Olá, Mundo!')
#
#     EXERCICIO 002
#
# nome = input('digite seu nome: ')
# print("É um prazer te conhecer, \033[31m{}\033[m!".format(nome))

#     EXERCICIO 003
#
# n1 = float(input('digite um numero: '))
# n2 = float(input('digite outro numero: '))
# soma = n1+n2
# print('a soma entre \033[1;32m{}\033[m e \033[1;32m{}\033[m é: \033[1;31m{}!'.format(n1, n2, soma))
#
#     EXERCICIO 004
#
# caractere = (input('informe algo: '))
# print('\033[4;34mAnalizando o que foi digitado!!\033[m')
# print(type(caractere))
# print('É um caractere?\033[4;36;40m{}\033[m'.format(caractere.isdigit()))
# print('É decimal? \033[4;36;40m{}\033[m'.format(caractere.isdecimal()))
# print('É um numero? \033[4;36;40m{}\033[m'.format(caractere.isnumeric()))
# print('É tudo minusculo? \033[4;36;40m{}\033[m'.format(caractere.islower()))
# print('É tudo numero? \033[4;36;40m{}\033[m'.format(caractere.isalnum()))
# print('É alfabetico?\033[4;36;40m{}\033[m '.format(caractere.isalpha()))
# print('É somente espaços? \033[4;36;40m{}\033[m'.format(caractere.isspace()))

#       AULA 07
#     EXERCICIO 005

# numero = int(input('digite um numero'))
# ant = numero - 1
# suc = numero + 1
# print('numero \033[34m{}\033[m, seu antecessor é \033[31m{}\033[m e o sucessor é \033[31m{}\033[m '.format(numero, ant, suc))

#     EXERCICIO 006


# numb = int(input('digite um numero'))
# raiz = numb**(1/2)
# dob = numb*2
# tri = numb*3
# print('numero \033[35m{}\033[m \nsua raiz \033[1;33m{}\033[m \nseu dobro \033[1;33m{}\033[m \nseu triplo \033[1;33m{}'.format(numb, raiz, dob, tri))

#     EXERCICIO 007


# n1 = int(input('nota numero 1'))
# n2 = int(input('nota numero 2'))
# print('Nota 1: \033[32m{}\033[m\nNota 2: \033[32m{}\033[m \nMédia: \033[1;30m{}\033[m'.format(n1, n2, (n1 + n2)/2))

#     EXERCICIO 008


# numero = int(input('Informe o tamanho em metros'))
# km = numero/1000
# hm = numero/100
# dam = numero/10
# dec = numero*10
# mil = numero*1000
# cen = numero*100
# print('Numero: \033[34m{}\033[m \nEm kilometros \033[1;32m{}\033[m \nEm Hectometros \033[1;32m{}\033[m \nEm Decametros \033[1;32m{}\033[m \nEm decimetros \033[1;31m{}\033[m\nEm milimetros: \033[1;31m{}\033[m\nEm centimetros: \033[1;31m{}\033[m'.format(numero, km, hm, dam, dec, mil, cen))

#     EXERCICIO 009

# a= int(input('Informe  um numero: '))
# n1 = a*1
# n2 = a*2
# n3 = a*3
# n4 = a*4
# n5 = a*5
# n6 = a*6
# n7 = a*7
# n8 = a*8
# n9 = a*9
# n10 = a*10
# print("\033[34m=\033[m" *12)
# print("\033[1;31mTabuada\033[m\n\033[1;35m{:2}x 1 = {:2}\n{:2}x 2 = {:2}\n{:2}x 3 = {:2}\n{:2}x 4 = {:2}\n{:2}x 5 = {:2}\n{:2}x 6 = {:2}\n{:2}x 7 = {:2}\n{:2}x 8 = {:2}\n{:2}x 9 = {:2}\n{:2}x10 = {:2}\033[m".format(a, n1, a, n2, a, n3, a, n4, a, n5, a, n6, a, n7, a, n8, a, n9, a, n10))
# print("\033[34m=\033[m" *12)

#     EXERCICIO 010


# real = float(input('Quantos reais você tem? '))
# dolar = float(input('quanto custa um dolar? '))
# print('Você pode comprar \033[36m{:.3f}\033[m dolar(es) com \033[34m{}\033[m R$'.format(real/dolar, real))

#     EXERCICIO 011


# larg = float(input('informe a largura: '))
# alt = float(input('informe a atura: '))
# m2 = float(larg * alt)
# tinta = m2/2
# pt = tinta*7
# print('Numa parede de {}{}{}m² você usará {}{:.3f}{} litro(s) de tinta, e gastará em media {}{:.3f}{} reais'.format( cores['verm'], m2, cores['limpa'], cores['azul'], tinta, cores['limpa'], cores['amar'], pt, cores['limpa']))

#     EXERCICIO 012


# prod = float(input('Qual o preço do produto? '))
# desc = prod/100*95
# print('preço atual {}{}{} reais\npreço com 5% de desconto {}{}{} reais'.format(cores['verm'], prod, cores['limpa'], cores['amar'], desc, cores['limpa'],))

#     EXERCICIO 013

# sal = float(input('informe seu salario: '))
# aum = sal+sal/100*15
# print('salário atual {}{}{} reais\nSalario liquido {}{}{} reais'.format(cores['verm'], sal, cores['limpa'], cores['amar'], aum, cores['limpa'],))


#     EXERCICIO 014

# c = float(input('Informe a temperatura em C°: '))
# f = 9 * c / 5 + 32
# print('A temperatura {}{}{}C° corresponde a {}{}{} F°'.format(cores['br'], c, cores['limpa'], cores['azul'], f, cores['limpa'],))

#     EXERCICIO 015

# dias = int(input('informe os dias alugado: '))
# km = float(input('informe os kms percorridos: '))
# total = (km * 0.15) + (dias * 60)
# print('O aluguel custou {}{:.2f}{} Reais'.format(cores['azul'], total, cores['limpa'],))

#      AULA 08
#    EXERCICIO 16


# n = float(input('Digite um numero: '))
# print('o numero {}{}{} tem a sua parte inteira {}{}{}'.format(cores['azul'], n, cores['limpa'], cores['verm'], math.floor(n), cores['limpa'],))

#   EXERCICIO 017
#
# copo = float(input('Informe o cateto oposto: '))
# cadj = float(input('Informe o cateto adjacente: '))
# hipo = (copo**2 + cadj**2)**(1/2)
# print('o comprimento da Hipotenusa é: {}{:.2f}{}'.format(cores['verm'], hipo, cores['limpa']))

#  2° modo
# copo = float(input('Informe o cateto oposto'))
# cadj = float(input('Informe o cateto adjacente'))
# hipo = math.hypot(copo, cadj)
# print('o comprimento da Hipotenusa é: {}{:.2f}{}'.format(cores['verm'], hipo, cores['limpa']))

#   EXERCICIO 018

# ang = float(input('informe o angulo desejado: '))
# sen = math.sin(math.radians(ang))
# cos = math.cos(math.radians(ang))
# tnj = math.tan(math.radians(ang))
# print('O seno de {}{}{} é {}{:.2f}{}\no cosseno de {}{}{} é {}{:.2f}{}\na tanjente de {}{}{} é {}{:.2f}{}'.format(cores['br'], ang, cores['limpa'], cores['azul'], sen, cores['limpa'], cores['br'], ang, cores['limpa'], cores['verm'], cos, cores['limpa'], cores['br'], ang, cores['limpa'], cores['amar'], tnj, cores['limpa']))

#   EXERCICIO 019

# aluno1 = input('nome do primeiro aluno: ')
# aluno2 = input('nome do segundo aluno: ')
# aluno3 = input('nome do terceiro aluno: ')
# aluno4 = input('nome do quarto aluno: ')
# lista = [aluno1, aluno2, aluno3, aluno4]
# escolha = random.choice(lista)
# print('O(a) aluno(a) sorteado foi {}{}{}'.format(cores['azul'], escolha, cores['limpa'],))

#   EXERCICIO 020

# a1 = input('primeiro aluno')
# a2 = input('segundo aluno')
# a3 = input('terceiro aluno')
# a4 = input('quarto aluno')
# lista1 = [a1, a2, a3, a4]
# random.shuffle(lista1)
# print('a ordem de apresentação será: {}{}{}'.format(cores['br'], lista1, cores['limpa'],))

#   EXERCICIO 021

# pygame.init()
# pygame.mixer.music.load('alok.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()

#     Alula 09
#   EXERCICIO 022

# nome = str(input('Digite seu nome: ')).strip()
# print('Seu nome em Maiusculo: {}'.format(nome.upper()))
# print('Seu nome em Minusculo: {}'.format(nome.lower()))
# name = nome.split()
# print('Seu nome tem {} letras e seu primeiro nome tem {} letras e é {}'.format(len(nome)-nome.count(' '), len(name[0]), name[0]))

#   EXERCICIO 023

# n = int(input('digite um numero de 0 a 9999: '))
# u = n // 1 % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000 % 10
# print('Unidade {}'.format(u))
# print('Dezena {}'.format(d))
# print('Centena {}'.format(c))
# print('Milhar {}'.format(m))

#   EXERCICIO 024

# cidade = str(input('informe o nome da sua cidade: ')).strip().title()
# print(cidade[:5] == 'Santo')

#   EXERCICIO 025

# nome = str(input('Informe seu nome: ')).strip().title()
# f = 'Silva' in nome
# print('Seu nome tem Silva? {}'.format(f))

#   EXERCICIO 026

# frase = str(input('Informe a frase: ')).upper().strip()
# q = frase.count('A')
# print('A letra (A) aparece {} vezes'. format(q))
# p1 = frase.find('A')+1
# print('1° Posiçao: {}'.format(p1))
# p2 = frase.rfind('A')+1
# print('Ultima Posiçao: {}'.format(p2))

#   EXERCICIO 027

# nome = str(input("Qual seu nome: ")).strip().title()
# name = nome.split()
# print('Ola, seu primeiro nome é: {}'.format(name[0]))
# print('E seu ultimo nome é: {}'.format(name[len(name)-1]))

#     Aula 10
#   EXERCICIO 028

# comp = int(random.randint(1, 5))
# print('Vou pensar em um numero entre 0 e 5...')
# usu = int(input('Em que numero o computador pensou? '))
# print('PROCESSANDO...')
# time.sleep(3)
# if comp == usu:
#     print('=' * 12 )
#     print('Acertou Parabéns!!')
#     print('=' * 12)
# else:
#     print('=' * 12)
#     print('Errou, Tente novamente!')
#     print('=' * 12)
# print('O computador pensou {}\nVocê digitou {}'.format(comp, usu))

#   EXERCICIO 029

# vel = float(input('Informe a Velocidade: '))
# if vel > 80:
#     print('Voce foi multado! O limite de velocidade é 80km/h')
#     print('A Multa custará: {} Reais'.format((vel-80)*7))
# print('Dirija com cuidado!')

#    EXERCICIO 030

# numero = int(input('Informe um numero: '))
# print('Analizando o Numero {}'.format(numero))
#
# if numero % 2 == 0:
#     print("O numero {}, é PAR".format(numero))
# else:
#     print('O numero {}, é IMPAR'.format(numero))


#    EXERCICIO 031

# km = float(input("Informe a distancia da viajem: "))
#
# if km <= 200:
#     print('Sua passagem custará {} reais'.format(km * 0.50))
# else:
#     print('Sua passagem custará {} Reais'.format(km * 0.45))

# 2° Modo

# km = float(input('Informe a distancia da sua viajem: ')
# price = km * 0.50 if 200 >= km else km * 0.45
# print('sua passagem custará R${}'.format(price))


#  EXERCICIO 032

# ano = int(input('Qual ano deseja verificar? coloque 0 para analizar o atual! '))
# if ano == 0:
#     ano = datetime.date.today().year
# print('=+=' *20)
# print('O Ano {} é um ano Bissexto??'.format(ano))
# print('=+=' *20)
# if ano % 4 == 1 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano {} É BISSEXTO!'.format(ano))
# else:
#     print('O ano {} NAO É BISSEXTO'.format(ano))

#   EXERCICIO 033
#
# n1 = int(input("Numero 1: "))
# n2 = int(input('Numero 2: '))
# n3 = int(input('Numero 3: '))
#
# if n1 > n2 and n3 < n1:
#     maior=n1
#     print('O Maior valor foi {}'.format(n1))
#
# if n2 > n1 and n3 < n2:
#     maior = n2
#     print('O Maior valor foi {}'.format(n2))
#
# if n3 > n2 and n1 < n3:
#     maior = n3
#     print("O Maior valor foi {}".format(n3))
#
# if n1 < n2 and n3 > n1:
#     menor = n1
#     print('O Menor valor foi {}'.format(n1))
#
# if n2 < n3 and n1 > n2:
#     menor = n2
#     print('O Menor valor foi {}'.format(n2))
#
# if n3 < n2 and n1 > n3:
#     menor = n3
#     print('O Menor valor foi {}'.format(n3))
#
# print('==+' * 20)
# print('O Menor digitado foi {} '.format(menor))
# print('O Maior digitado foi {} '.format(maior))
#
#
# EXERCICIO 034
#
# salario = float(input('Insira o salário: '))
# if salario > 1250.00:
#     novo = salario + (salario*10/100)
# else:
#     novo = salario + (salario*15/100)
#
# print('Seu salário reajustado será R$ {}'.format(novo))
#
#  EXERCICIO 035
#
# a = float(input('Reta um: '))
# b = float(input('Reta dois: '))
# c = float(input('Reta tres: '))
# print('Verificando se essas medidas\npodem formar um triangulo...')
# print("=" *20)
# bc = b - c
# ac = a - c
# ab = a - b

# Forma completa...

# if bc < a < b + c:
#     print('verificando...')
#
# if ac < b < a + c:
#     print('verificando...')

# Forma simplificada...
# print("=" *20)
#
# if ab < c < a + b and ac < b < a + c and bc < a < b + c:
#     print('SIM, podem formar um triangulo!')
# else:
#     print('NAO podem formar um triangulo!')
#
# if a == b == c:
#     print("Essas medidas formam um triangulo perfeito")
#
#     ======= MUNDO 02=========
#
#      AULA 11
