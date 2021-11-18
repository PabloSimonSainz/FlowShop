from utils import generar_permutador, funcion_f, tiempo_final_f
import random
import numpy as np
from matplotlib import pyplot as plt

def rand_search(d, iter, plot: bool = True):
    actual_sol = generar_permutador(d)
    actual_time = tiempo_final_f(funcion_f(actual_sol, d))
    data = []

    for i in range(iter):
        new_sol = generar_permutador(d)
        new_time = tiempo_final_f(funcion_f(new_sol, d))
        data.append(actual_time)
        
        if new_time < actual_time:
            actual_sol = new_sol
            actual_time = new_time
    
    if plot:
        plt.plot(list(range(len(data))), data)
        plt.grid(b=True)
        
        plt.xlabel('Iteración')
        plt.ylabel('Score')
        
        plt.title('Búsqueda Aleatoria')
    
    return actual_sol

def get_vecino(v):
    for i in range(len(v)):
        for j in range(i):
            aux = list(v)
            aux[i], aux[j] = aux[j], aux[i]
            yield aux

def local_search(d, primero = bool, actual_sol = None, plot: bool = True):
    if actual_sol == None:
        actual_sol = generar_permutador(d)
    actual_time = tiempo_final_f(funcion_f(actual_sol, d))
    data = []
    while True:
        aux = actual_sol
        data.append(actual_time)
        for i in get_vecino(actual_sol):
            new_sol = i
            new_time = tiempo_final_f(funcion_f(new_sol, d))

            if new_time < actual_time:
                actual_sol = new_sol
                actual_time = new_time
                if primero: # local primero
                    break

        if aux == actual_sol: break

    if plot:
        plt.plot(list(range(len(data))), data)
        plt.grid(b=True)
        
        plt.xlabel('Iteración')
        plt.ylabel('Score')
        
        plt.title('Búsqueda Local')
    
    return actual_sol


def recocido_simulado(d, iteraciones = 50, sec_enfriamiento = 0.8, temp_final = 0.1, plot: bool = True):
    
    sol_actual = generar_permutador(d)
    temp_inicial = 0.35 * tiempo_final_f(funcion_f(sol_actual, d))
    temp = temp_inicial
    data = []
    while temp >= temp_final:
        for i in range(iteraciones):
            sol_candidata = random.choice(list(get_vecino(sol_actual)))
            tiempo_actual = tiempo_final_f(funcion_f(sol_actual, d))
            data.append(tiempo_actual)
            tiempo_candidata = tiempo_final_f(funcion_f(sol_candidata, d))
            
            if tiempo_candidata < tiempo_actual:
                sol_actual = sol_candidata
                tiempo_actual = tiempo_candidata
                
            else:
                rand = random.random()
                if rand <= np.exp((tiempo_actual - tiempo_candidata) / temp):
                    sol_actual = sol_candidata
                    tiempo_actual = tiempo_candidata
        
        temp = sec_enfriamiento * temp
    
    if plot:
        plt.plot(list(range(len(data))), data)
        plt.grid(b=True)
        
        plt.xlabel('Iteración')
        plt.ylabel('Score')
        
        plt.title('Recocido Simulado')
    
    return sol_actual