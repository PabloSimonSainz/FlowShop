from utils import generar_permutador, funcion_f, tiempo_final_f
import matplotlib.pyplot as plt
import seleccion, cruces

def genetic(d, NIND: int=20, NGEN: int=100, MUPB: float=0.2, CXPB: float=0.7, OX:bool =True, plot: bool=True):
    individuos = []
    retorno = []
    bestfit = -1
    dmin, davg, dmax = [], [], []
    
    # Creamos la población
    for i in range(NIND):
        individuos.append(generar_permutador(d))
    
    for i in range(NGEN):
        fitness = []
        for i in individuos:
            fitness.append(tiempo_final_f(funcion_f(i, d)))
        
        aux = min(fitness)
        if bestfit > aux or bestfit == -1:
            bestfit = aux
            retorno = individuos[fitness.index(bestfit)]
        dmin.append(min(fitness))
        davg.append(sum(fitness)/len(fitness))
        dmax.append(max(fitness))

        # Seleccionamos
        #individuos = seleccion.ruleta(individuos=individuos, fitness=fitness, seleccionados=NIND)
        #individuos = seleccion.estocastico(individuos=individuos, fitness=fitness, seleccionados=NIND)
        individuos = seleccion.torneo(individuos=individuos, fitness=fitness, seleccionados=NIND, participantes=3)
        #individuos = seleccion.ranking(individuos=individuos, fitness=fitness, seleccionados=NIND)
        
        # Cruzamos
        individuos = cruces.cruce(individuos = individuos, OX=OX, CXPB=CXPB)
        
        # Mutamos
        cruces.mutacion(individuos=individuos, MUPB=MUPB, times = 1)
    
    if plot:
        plt.plot(list(range(len(dmin))), dmin)
        plt.plot(list(range(len(davg))), davg)
        plt.plot(list(range(len(dmax))), dmax)
        plt.grid(b=True)
        
        plt.xlabel('Population')
        plt.ylabel('Fitness')
        
        plt.title('Genetic Algorithm')
    
    return retorno