import organizador
import random 
import numpy as np

# ---------------------------------------------------------------------------------------------------------------

def busqueda_aleatoria():
    
    sol_inicial = generar_permutador()
    sol_actual = sol_inicial
    sol_mejor = sol_actual
    print("Partimos de la siguiente solución: ")
    print(sol_inicial)
    # Pedimos por teclado el número de intentos
    x = int(input("Introduce el número de iteraciones: "))
    optimo_mejor = funcion_f(sol_mejor)
    
    for i in range(x):
        sol_actual = generar_permutador()
        optimo = funcion_f(sol_actual)    
        if(optimo > optimo_mejor):
            sol_mejor = sol_actual
            optimo_mejor = optimo
        
    print("La mejor solución es: ")
    print(sol_mejor)
    print("Con valor: ")
    print(optimo_mejor)
   
# ---------------------------------------------------------------------------------------------------------------

def busqueda_local():
    
    sol_inicial = generar_permutador()
    sol_actual = sol_inicial
    sol_mejor = sol_actual
    vecino = []
   
    for i in range(len(sol_actual)):
        for j in range(len(sol_actual)):
            mov = sol_actual[:]
            # print(mov)
            # print(sol_actual)           
            aux = mov[i]
            mov[i] = mov[j]
            mov[j] = mov[i]
            mov[j] = aux
            vecino.append(mov)
    return vecino

# ---------------------------------------------------------------------------------------------------------------

def generar_aleatorio(solucion):
    for i in range(0,2):
        indice_aleatorio = random.randint(0, len(solucion) - 1)
        a = random.randint(0, len(solucion) - 1)
        temporal = solucion[a]
        solucion[a] = solucion[indice_aleatorio]
        solucion[indice_aleatorio] = temporal
    return solucion

# ---------------------------------------------------------------------------------------------------------------

def recocido_simulado(sec_enfriamiento,iteraciones,temp_final):
    
    sol_actual = generar_permutador()
    temp_inicial = 0.35 * funcion_f(sol_actual)
    temp = temp_inicial
    while temp >= temp_final:
        for i in range(1,iteraciones):
            sol_candidata = generar_aleatorio(sol_actual)
            coste = funcion_f(sol_candidata)-funcion_f(sol_actual)
            if coste < 0:
                sol_actual = sol_candidata
            else:
                rand = random.random()
                if rand <= np.index_exp(-coste/temp):
                    sol_actual = sol_candidata
    temp = sec_enfriamiento*temp

    return sol_actual

# ---------------------------------------------------------------------------------------------------------------