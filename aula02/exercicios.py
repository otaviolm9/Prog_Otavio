"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
    nova_lista = []
    contador = 0

    while contador < len(lista): 
        if lista[contador] >= 0:
            nova_lista.append(lista[contador])  
        contador += 1 
        
    return nova_lista

def inverte(lista):
    nova_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[i])
    return nova_lista


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


def intercala(lista_a, lista_b):
    return [item for par in zip(lista_a, lista_b) for item in par]



def remove_repetidos(lista):
    """(Desafio) Devolve uma lista nova sem repetidos,
    mantendo a ordem da primeira aparicao."""
    pass
