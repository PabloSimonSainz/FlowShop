import random
# PROBABILISTICOS

def ruleta(individuos, fitness, seleccionados: int):
    totalf = sum(fitness)
    q = []
    
    aux = 0
    for i in fitness:
        aux += (totalf-i)/totalf
        q.append(aux)
        
    retorno = []
    
    for i in range(seleccionados):
        r = random.random()
        aux = 0
        for j in q:
            if r < j:
                retorno.append(individuos[aux])
                break
            aux += 1
    
    return retorno

def torneo(individuos, fitness, seleccionados: int, participantes:int=3):
    retorno = []
    for i in range(seleccionados):
        champs = []
        
        for j in range(participantes):
            champs.append(random.choice(fitness))
            
        retorno.append(individuos[fitness.index(min(champs))])

    return retorno
            

# DETERMINISTAS
def ranking(individuos, fitness, seleccionados: int):
    individuos = [x for _,x in sorted(zip(fitness,individuos))]
    fitness = sorted(fitness)
    return individuos[0:seleccionados]