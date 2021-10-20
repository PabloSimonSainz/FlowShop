from numpy import string_
import algoritmos

class Organizador:
    def __init__(self, file, vector = None):
        self._d = algoritmos.read_file(file)

        self._v = vector
        if vector == None:
            self._v = algoritmos.generar_permutador(self._d)

        self._f = algoritmos.funcion_f(self._v, self._d)

    def get_d(self):
        return self._d

    def get_v(self):
        return self._v

    def get_f(self):
        return self._f

    def __str__(self):
        ret = "d: " + "\n"
        for i in self._d:
            ret += str(i) + "\n"
        ret += "v: " + str(self._v) + "\n"
        ret += "f: " + "\n"
        for i in self._f:
            ret += str(i) + "\n"
        return ret
        
