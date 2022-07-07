# Programação Orientada a Objetos
# Números especiais



def eh_primo(n):
    if n < 2:
        return False
    qtd_divisores = 0
    i = 1
    while i <= n:
        if n % i == 0:
            qtd_divisores += 1
        i += 1
    if qtd_divisores == 2:
        return True
    else:
        return False


def lista_primos(n):
    if n < 2:
        False
    lista = []
    i = 2
    for i in range(2, n+1):
        if eh_primo(i) == True:
            lista.append(i)
    return lista


def conta_primos(s):
    dicionario = {}
    for item in s:
        if eh_primo(item) == True:
            if item in dicionario:
                dicionario[item] += 1
            else:
                dicionario[item] = 1
    return dicionario


def eh_armstrong(n):
    num = len(str(n))
    soma = 0
    i = n
    while i > 0:
        digito = i % 10
        soma = soma + (digito**num)
        i = i//10
    if soma == n:
        return True
    else:
        return False


def eh_quase_armstrong(n):
    if eh_armstrong(n) == True:
        return False
    else:
        num = len(str(n))
        soma = 0
        i = n

        while i > 0:
            digito = i % 10
            soma = soma + (digito**num)
            i = i//10
        if soma == n or soma - 1:
            return True
        else:
            return False

def lista_armstrong(n):
    lista = []
    for i in range(0, n):
        if eh_armstrong(i) == True:
            lista.append(i)
    return lista


def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        divisor = n % i
        if divisor == 0:
            soma = soma + i
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for i in range(1, n):
        if eh_perfeito(i) == True:
            lista.append(i)
    return lista
