"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    return soma


def conta_pares(lista):
    contador = 0
    for num in lista:
        if num % 2 == 0:
            contador += 1
    return contador


def maior_valor(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior


def existe(lista, alvo):
    for item in lista:
        if item == alvo:
            return True
    return False


def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def segundo_maior(lista):
    maior = lista[0]
    segundo = lista[1]
    if segundo > maior:
        maior, segundo = segundo, maior
    for i in range(2, len(lista)):
        num = lista[i]
        if num > maior:
            segundo = maior
            maior = num
        elif num > segundo:
            segundo = num
    return segundo
