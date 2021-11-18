
import random
import csv


def read_file(file = "Data\\ejem_clase1.txt"):
    """
    Completar.
    Función que lee un archivo y almacena en una variable el numero de maquinas
    en otra las órdenes y en una matriz ambas dos.
    """
    """
    archivo = 'Doc1.txt'
    
    f = open(archivo)
    print(f.read())
    f.close()
    """
    
    with open(file, newline = '') as f:
        reader = csv.reader(f)
        data = list(reader)

    datos = []
    
    for i in range(len(data)):
        datos.append(data[i][0].split())
        
        for j in range(len(datos[i])):
            datos[i][j] = int(datos[i][j])

    retorno = []
    for tarea in range(datos[0][0]):
        retorno.append([])
        for maquina in range(datos[0][1]):
            retorno[tarea].append(datos[tarea+1][maquina*2+1])

    return retorno

def generar_permutador(matriz_datos = read_file()):
    
    ordenes = [i for i in range(len(matriz_datos))]
    retorno = []
    
    while len(ordenes) != 0:
        rand = random.randint(0, len(ordenes) - 1)
        retorno.append(ordenes[rand])
        ordenes.pop(rand)

    return retorno


def funcion_f(vector = generar_permutador(), datos = read_file()):
    ntar = len(datos)
    nmaq = len(datos[0])
    retorno = [[0 for j in range(nmaq)] for i in range(ntar)]
    puntero = [0 for i in range(nmaq)]

    for t in vector:
        for m in range(nmaq):
            if m == 0:
                retorno[t][m] = datos[t][m] + puntero[m]
                puntero[m] = retorno[t][m]
            else:
                if puntero[m-1] > puntero[m]:
                    retorno[t][m] = datos[t][m] + puntero[m-1]
                else:
                    retorno[t][m] = datos[t][m] + puntero[m]

                puntero[m] = retorno[t][m]

    return retorno

def tiempo_final_f(f):
    mx = 0
    for i in f:
        aux = max(i)
        if aux > mx:
            mx = aux

    return mx

def get_fichero(n = None):
    documentos = ["ejem_clase1.txt","ejem_clase2.txt"]
    documentos += ["Doc" + str(i+1) + ".txt" for i in range(11)]
    texto = "Elija el problema a resolver: \n"
    aux = ["\t" + str(i + 1) + ". " + str(documentos[i]) + "\n" for i in range(11)]

    for i in range(11):
        texto += aux[i]

    if n == None:
        n = int(input(texto))

    return "Data\\" + documentos[n - 1]