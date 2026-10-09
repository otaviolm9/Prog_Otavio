"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador


def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


def sem_o_maior(lista):
    if not lista:
        return []
        
    indice_maior = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = i
            
    nova_lista = []
    for i in range(len(lista)):
        if i != indice_maior:
            nova_lista.append(lista[i])
            
    return nova_lista


def acumulada(lista):
    nova_lista = []
    soma_corrente = 0
    
    for numero in lista:
        soma_corrente += numero
        nova_lista.append(soma_corrente)
        
    return nova_lista


def achata(lista_de_listas):
    nova_lista = []
    for sublista in lista_de_listas:
        nova_lista += sublista
    return nova_lista



# ---------- Bloco 2: busca ----------

def busca_ultima(lista, alvo):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == alvo:
            return i
    return -1


def conta_ocorrencias(lista, alvo):
    contador = 0
    for elemento in lista:
        if elemento == alvo:
            contador += 1
    return contador


def primeiro_maior_que(lista, limite):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def busca_binaria_primeira(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    posicao_encontrada = -1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == alvo:
            posicao_encontrada = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return posicao_encontrada


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    soma = 0
    operacoes = 0
    
    for elemento in lista:
        operacoes += 1
        if elemento % 2 == 0:
            soma += elemento
            
    return (soma, operacoes)


def maior_contando(lista):
    maior = lista[0]
    comparacoes = 0
    
    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]
            
    return (maior, comparacoes)


def tem_soma_contando(lista, alvo):
    comparacoes = 0
    n = len(lista)
    
    for i in range(n):
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return (True, comparacoes)
                
    return (False, comparacoes)


def ordenada_contando(lista):
    comparacoes = 0
    n = len(lista)
    
    # Listas vazias ou com apenas 1 elemento já estão ordenadas por definição
    if n < 2:
        return (True, 0)
        
    for i in range(n - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return (False, comparacoes)
            
    return (True, comparacoes)


# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    lista.reverse()


def eh_palindromo(lista):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio < fim:
        if lista[inicio] != lista[fim]:
            return False
        inicio += 1
        fim -= 1
        
    return True


def par_que_soma(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio < fim:
        soma_atual = lista[inicio] + lista[fim]
        
        if soma_atual == alvo:
            return (inicio, fim)
        elif soma_atual < alvo:
            inicio += 1
        else:
            fim -= 1
            
    return (-1, -1)


def soma_maxima_janela(lista, k):
    if not lista or k <= 0 or k > len(lista):
        return 0
        
    soma_atual = sum(lista[:k])
    maior_soma = soma_atual
    
    for i in range(k, len(lista)):
        soma_atual = soma_atual + lista[i] - lista[i - k]
        if soma_atual > maior_soma:
            maior_soma = soma_atual
            
    return maior_soma


def parenteses_balanceados(texto):
    pilha = []
    pares = {')': '(', ']': '['}
    
    for caractere in texto:
        if caractere in '([':
            pilha.append(caractere)
        elif caractere in ')]':
            if not pilha or pilha[-1] != pares[caractere]:
                return False
            pilha.pop()
            
    return len(pilha) == 0
