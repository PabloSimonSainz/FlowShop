import random
from enum import Enum

def mutacion(individuos, MUPB: float,times: int=1):
    for i in range(len(individuos)):
        r = random.random()
        
        if r < MUPB:
            for i in range(times):
                i1, i2 = random.randint(0,len(individuos[i])-1), random.randint(0,len(individuos[i])-1)
                individuos[i][i1], individuos[i][i2] = individuos[i][i2], individuos[i][i1]
        
    return individuos

def cruce(individuos, OX: bool, CXPB: float):
    retorno = []
    index = []
    
    for i in range(len(individuos)):
        r = random.random()
        
        if r < CXPB:
            index.append(i)
        if len(index) == 2:
            if OX:
                #retorno.extend(ox([individuos[index[0]], individuos[index[1]]]))
                individuos[index[0]], individuos[index[1]] = ox([individuos[index[0]], individuos[index[1]]])
            else:
                #retorno.extend(cx([individuos[index[0]], individuos[index[1]]]))
                individuos[index[0]], individuos[index[1]] = cx([individuos[index[0]], individuos[index[1]]])
            index = []
    
    return individuos


def ox(pareja):
    puntos = [random.randint(0, len(pareja[0]) - 1), random.randint(0, len(pareja[0]) - 1)]
    puntos.sort()
    retorno = [list(pareja[0]), list(pareja[1])]
    
    for k in range(2):
        bloque = list(pareja[k][puntos[0]:puntos[1]])
        aux = 0
        for i in range(len(pareja[0])):
            if pareja[k][i] not in bloque:
                for i in range(aux, len(pareja[0])):
                    if pareja[not k][i] not in bloque:
                        retorno[k][i] = pareja[not k][i]
                        aux = i + 1
                        break
    return retorno

def cx(pareja):
    r = random.randint(0, len(pareja[0])-1)
    ciclo = [pareja[0][r], pareja[1][r]]
    retorno = [list(pareja[0]), list(pareja[1])]
    
    if ciclo[0] != ciclo[1]:
        for i in pareja[0]:
            index = pareja[0].index(ciclo[-1])
            if pareja[1][index] == ciclo[0]:
                break
            ciclo.append(pareja[1][index])
    else:
        ciclo.pop()
    
    for k in range(2):

        aux = 0
        for i in range(len(pareja[0])):
            if pareja[k][i] not in ciclo:
                for i in range(aux, len(pareja[0])):
                    if pareja[not k][i] not in ciclo:
                        retorno[k][i] = pareja[not k][i]
                        aux = i + 1
                        break

    return retorno

