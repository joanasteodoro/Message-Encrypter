#86440 - Joana Teodoro

from math import sqrt

#VERSAO SIMPLIFICADA

def gera_chave1 (letras): 
    #gera 5 tuplos, cada um com 5 elementos do tuplo letras
    tuplo = ()
    nrtuplos = 0
    a = 0
    b = 5
    while 25 != nrtuplos**2:
        nrtuplos = nrtuplos + 1 #criacao de novo tuplo
        tuplo = tuplo + (letras[a:b], )
        a, b = a + 5, b + 5 #incrementar indices para que cada tuplo contenha 5 elementos
    return tuplo 

def obtem_codigo1 (car, chave): 
    #funcao que obtem o codigo de um caractere
    for lin in range(len(chave)):
        for col in range(len(chave[lin])):
            if chave[lin][col] == car:
                return str(lin) + str(col)

def codifica1(cad, chave): 
    #funcao que codifica uma cadeia de caracteres
    codigo = ''
    for i in cad:
        codigo = codigo + obtem_codigo1(i, chave)
    return codigo

def obtem_car1(cod, chave): 
    #funcao que obtem o caractere pertencente a chave a partir do codigo
    for lin in range(len(chave) + 1):
        for col in range(len(chave) + 1):
            if cod == str(lin) + str(col):
                return chave[lin][col]

def descodifica1(cad_codificada,chave): 
    #funcao que descodifica uma cadeia de caracteres
    cadfinal = ''
    for i in range(0, len(cad_codificada), 2): #atribuicao de 2 numeros a cada caractere correspondentes a linha e a coluna 
        decode = str(cad_codificada[i]) + str(cad_codificada[i + 1])
        cadfinal = cadfinal + obtem_car1(decode, chave)
    return cadfinal


#VERSAO FINAL

def gera_chave2 (letras):
    tuplo = ()
    i = 0
    nrelementos = round (sqrt (len(letras))) #numero de elementos que cada tuplo vai ter
    if len(letras) % nrelementos != 0: #contagem do numero de tuplos
        nrelementos_2 = int(sqrt(len(letras)))
        nrtuplos = nrelementos_2 + 1
    else:
        nrtuplos = nrelementos
    elementos = nrelementos #guarda a variavel nrelementos para utilizacao no indice do tuplo
    while nrtuplos >= 0:
        if nrtuplos > 0:
            nrtuplos = nrtuplos - 1
            tuplo = tuplo + (letras[i:nrelementos], )
            i = nrelementos
            nrelementos = nrelementos + round(sqrt (len(letras)))                        
        else:
            nrtuplos = nrtuplos - 1
            i = (elementos - 1) * nrelementos
            tuplo = tuplo + (letras[i:])
    return tuplo

def obtem_codigo2 (car, chave): 
    #funcao que obtem o codigo de um caractere da chave 
    if (obtem_codigo1 (car, chave) == None): #adicionar possibilidade de o argumento car nao pertencer a chave
        return 'XX'
    else:
        return obtem_codigo1(car,chave)

def codifica2(cad, chave):
    #funcao que codifica uma cadeia de caracteres para qualquer numero de caracteres na chave
    codigo = ''
    for i in cad:
        codigo = codigo + obtem_codigo2(i, chave)
    return codigo

def obtem_car2(cod, chave):
    #funcao que obtem o caractere pertencente a chave a partir do codigo de dois digitos referentes a linha e coluna
    if (obtem_car1(cod, chave) == None): #adicionar possibilidade de o argumento codigo nao pertencer a chave
        return '?'
    else:
        return obtem_car1(cod, chave)

def descodifica2 (cad_codificada,chave): 
    #funcao que descodifica uma cadeia de caracteres independentemente do numero de elementos na chave
    cadeia = ''
    for i in range(0, len(cad_codificada), 2):
        descod = str(cad_codificada[i]) + str(cad_codificada[i + 1])
        cadeia = cadeia + obtem_car2(descod, chave)
    return cadeia