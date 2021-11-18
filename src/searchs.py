from utils import generar_permutador, funcion_f, tiempo_final_f
import random
import numpy as np

def rand_search(d, iter):
    actual_sol = generar_permutador(d)
    actual_time = tiempo_final_f(funcion_f(actual_sol, d))

    for i in range(iter):
        new_sol = generar_permutador(d)
        actual_time = tiempo_final_f(funcion_f(new_sol, d))

        if new_sol > actual_sol:
            actual_sol = new_sol
            
    return actual_sol

def get_vecino(v):
    for i in range(len(v)):
        for j in range(i):
            aux = list(v)
            aux[i], aux[j] = aux[j], aux[i]
            yield aux

def local_search(d, primero = bool, actual_sol = None):
    if actual_sol == None:
        actual_sol = generar_permutador(d)
    actual_time = tiempo_final_f(funcion_f(actual_sol, d))

    while True:
        aux = actual_sol
        for i in get_vecino(actual_sol):
            new_sol = i
            new_time = tiempo_final_f(funcion_f(new_sol, d))

            if new_time > actual_time:
                actual_sol = new_sol
                actual_time = new_time
            if primero: # local primero
                break

        if aux == actual_sol: break

    return actual_sol


def recocido_simulado(d, iteraciones = 50, sec_enfriamiento = 0.8, temp_final = 0.1):
    
    sol_actual = generar_permutador(d)
    temp_inicial = 0.35 * tiempo_final_f(funcion_f(sol_actual, d))
    temp = temp_inicial

    while temp >= temp_final:
        for i in range(iteraciones):
            sol_candidata = random.choice(list(get_vecino(sol_actual)))

            coste = tiempo_final_f(funcion_f(sol_candidata, d)) - tiempo_final_f(funcion_f(sol_actual, d))
            
            if coste < 0:
                sol_actual = sol_candidata
            else:
                rand = random.random()
                if rand <= np.exp(-coste / temp):
                    sol_actual = sol_candidata
        
        temp = sec_enfriamiento * temp
    return sol_actual