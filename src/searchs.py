import numpy as np
import random

from initial import generar_permutador, funcion_f, tiempo_final_f

def rand_search(d, iter):
    actual_sol = generar_permutador(d)
    actual_time = tiempo_final_f(funcion_f(actual_sol, d))

    for i in range(iter):
        new_sol = generar_permutador(d)
        new_time = tiempo_final_f(funcion_f(new_sol, d))

        if new_time > actual_time:
            actual_sol = new_sol
            actual_time = new_time
            
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



# ---------------------------------------------------------------------------------------------------------------

def recocido_simulado(sec_enfriamiento, d, temp_final, iteraciones = 50):
    
    sol_actual = generar_permutador(d)
    temp_inicial = 0.35 * funcion_f(sol_actual, d)
    temp = temp_inicial

    while temp >= temp_final:
        for i in range(iteraciones):
            sol_candidata = random.choice(get_vecino(sol_actual))
            coste = funcion_f(sol_candidata, d) - funcion_f(sol_actual, d)
            
            if coste < 0:
                sol_actual = sol_candidata
            else:
                rand = random.random()
                if rand <= np.index_exp(-coste / temp):
                    sol_actual = sol_candidata
    temp = sec_enfriamiento * temp

    return sol_actual