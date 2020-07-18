import pandas as pd
import numpy as np 

def geraJogo():
    i = 1
    jogo = []
    while(i <= 15):
        num = np.random.randint(1, 25)
        if num not in jogo:
            jogo.append(num)
            i = i + 1     
    jogo.sort()
    return jogo


def readJogos():
    df = pd.read_excel("resultados.xlsx", header=None, skiprows=7, usecols= "C:Q")
  #  print(df.values)
    return df.values

def novoJogo():
    num_elementos_lista = len(jogos)
    x = 0
    while(x < num_elementos_lista-1):
        x+=1
        v = np.array(jogo) == np.array(jogos[x])
        # print('Meu jogo =', jogo)
        # print('Outro jo =', jogos[x])
        # print('any = ', v.any())
        # print('all = ', v.all())
        if (v.all()):
            return False
    return True

def qtdadeUltimoJogo():
    a = 0
    for j1 in range(15):
        for j2 in range(15):
            if (jogos[0][j1] == jogo[j2]):
                a+=1
            # print("\n")
            # print(jogos[0][j1])
            # print(jogo[j2])
    if (a >= 8 and a <= 10):
        return True 
    else: 
        return False

def qtdadePrimos():
    p = 0
    for j in range(15):
        if (jogo[j] == 2 or jogo[j] == 3 or jogo[j] == 5 
         or jogo[j] == 7 or jogo[j] == 11 or jogo[j] == 13 
         or jogo[j] == 17 or jogo[j] == 19 or jogo[j] == 23):
            p+=1
    if (p >= 4 and p <=7):
        return True
    else:
        return False

def qtdadeParesImpares():
    pares = 0
    impares = 0
    for j in range(15):
        if (jogo[j]%2) == 0:
            pares+=1
        else:
            impares+=1
    if ((pares == 7 and impares == 8) or (pares == 8 and impares ==7)):
        return True
    else:
        return False

def numerosPraxe():
    m = 0
    n = 0
    o = False
    p = False
    for j in range(15):
        if jogo[j] == 1:
            o = True
            for k in range(15):
                if (jogo[k] == 2 or jogo[k] == 3 or jogo[k] == 4):
                    m+=1
        if jogo[j] == 15:
            p = True
            for k in range(15):
                if (jogo[k] == 22 or jogo[k] == 23 or jogo[k] == 24 or jogo[k] == 25):
                    n+=1

    temOsDois = False
    temSoUm = False
    temSoQuinze = False
    nenhum = False

    if o and p:
        temOsDois = True
    if o and not p:
        temSoUm = True
    if not o and p:
        temSoQuinze = True
    if not o and not p:
        nenhum = True
        

    if temOsDois:
        if (m == 3 and n == 4):
            return True

    if temSoUm:
        if (m == 3):
            return True

    if temSoQuinze:
        if (n == 4):
            return True

    if nenhum:
        return True


jogoTop = False
novo = False
repetidos = False
primos = False
paresImpares = False
praxe = False

# Le planilha de jogos anteriores
jogos = readJogos()

while (not jogoTop):

    # Gera novo jogo
    jogo = geraJogo()

    # Verifica se jogo ja saiu
    novo = novoJogo()

    # Verifica quantidade de valores do ultimo jogo
    repetidos = qtdadeUltimoJogo()

    # Verifica quantidade de primos
    primos = qtdadePrimos()

    # Verifica quantidade de pares e impares
    paresImpares = qtdadeParesImpares()

    # Verifica se saiu o numero 1 ou 15 e segue as regras:
    # Quando a bola número 1 é sorteada, geralmente ela vem acompanha dos números 2, 3, e 4.
    # E quando o 15 for sorteado é praxe ser acompanhado pelos números 22, 23, 24 e 25.
    praxe = numerosPraxe()

    if (novo and repetidos and primos and paresImpares and praxe):
        jogoTop = True

if (jogoTop):
    print('JOGO TOP: ', jogo)
