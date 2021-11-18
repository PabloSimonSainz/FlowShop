import random
# PROBABILISTICOS

def ruleta(individuos, fitness, seleccionados: int):
    totalf = sum(fitness)
    q = []
    
    aux = 0
    for i in fitness:
        aux += i/totalf
        q.append(aux)
    print(q)
    retorno = []
    for i in range(seleccionados):
        r = random.random()
        print(r)
        for j in q:
            if r < j:
                retorno.append(individuos[aux])
                break
            aux += 1
    
    return retorno

# DETERMINISTAS
def ranking(individuos, fitness, seleccionados: int):
    individuos = [x for _,x in sorted(zip(fitness,individuos))]
    fitness = sorted(fitness)
    return individuos[0:seleccionados]