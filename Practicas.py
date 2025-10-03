"""
import numpy as np
def cantPares(arreglo:np.array,cont=0):
    if len(arreglo) == 1:
        return arreglo
    else:
        for i in range (len(arreglo)-1):
            if arreglo[i] % 2 == 0:
                cont += 1 
                print(cantPares)
                return cantPares (arreglo[1:],cont)
            
            

def mayoresQue(arreglo:np.array,cantMayores = 0, mayoresque = 10):
    if len (arreglo) == 1:
        return cantMayores
    else:
        mayores = mayoresQue(arreglo[1:],cantMayores+1)
        if arreglo[0] > mayores:
            return arreglo[0],cantMayores
        else:
            return cantMayores

def mayoresQueNum(arreglo:np.array) -> bool:
    if cantPares(arreglo) > mayoresQue(arreglo):
        return True
    else:
        return False
        
    
arr1 = [5, 10, 9, 8, 13, 21]

cantPares(arr1)
print(cantPares)



def cantPares(arreglo:np.array,contador = 0):
    if arreglo == 0: 
        return 0
    else:
        if arreglo[0] % 2 == 0:
            cantPares(arreglo+1)
            contador += 1 
        return cantPares(arreglo+1)

def mayoresQue10(arreglo:np.array) -> int:
    if len(arreglo) == 0:
        return 0 
    else:
        if arreglo[0] > 10:
            return 1 + mayoresque10(arreglo[1: ])
        else:
            return mayoresQue10(arreglo[1:])
        


def mayoresQue10(arreglo:np.array,contador = 0) -> int:
    if len(arreglo) == 0:
        return contador
    else:
        if arreglo[0] > 10:
            return mayoresque10(arreglo[1: ],contador+1)
        else:
            return mayoresQue10(arreglo[1:],contador)
        

    

        


                    

        import numpy as np
""" 

import numpy as np
class Auto:
    def __init__(self, patente, horaIngreso):
        self._patente = patente
        self._horaIngreso = horaIngreso

    def __repr__(self):
        return f"Auto({self._patente},{self._horaIngreso})"


class Estacionamiento:
    def __init__(self, tamaño):
        self._tamaño = tamaño
        # mantener 0 como marcador de vacío, pero usar dtype=object para poder almacenar Auto
        self._estacionamiento = np.full((self._tamaño, self._tamaño), 0, dtype=object)

    def estacionar(self, patente, horaIngreso):
        auto = Auto(patente, horaIngreso)
        for i in range(len(self._estacionamiento)):
            for j in range(len(self._estacionamiento[0])):
                if self._estacionamiento[i][j] == 0:   # lugar vacío
                    self._estacionamiento[i][j] = auto
                    return (i, j)
        # si recorrimos todo y no encontramos lugar:
        raise Exception('Estacionamiento lleno')

    def salir(self, patente):
        for i in range(len(self._estacionamiento)):
            for j in range(len(self._estacionamiento[0])):
                auto = self._estacionamiento[i][j]
                # comprobar que no sea el marcador de vacío y luego comparar patente
                if auto != 0 and getattr(auto, "_patente", None) == patente:
                    horaIngreso = auto._horaIngreso
                    self._estacionamiento[i][j] = 0
                    return horaIngreso
        # no encontrada la patente
        return None

    def estaVacio(self):
        # True solo si TODOS los lugares están vacíos (== 0)
        for i in range(len(self._estacionamiento)):
            for j in range(len(self._estacionamiento[0])):
                if self._estacionamiento[i][j] != 0:
                    return False
        return True

    def cantidadAutoHora(self, horaFinal, contador=0):
        # cuenta autos con horaIngreso < horaFinal
        for i in range(len(self._estacionamiento)):
            for j in range(len(self._estacionamiento[0])):
                auto = self._estacionamiento[i][j]
                if auto != 0:
                    horaIngreso = getattr(auto, "_horaIngreso", None)
                    if horaIngreso is not None and horaIngreso < horaFinal:
                        contador += 1
        return contador

    def __repr__(self):
        autos = ""
        for i in range(len(self._estacionamiento)):
            for j in range(len(self._estacionamiento[0])):
                auto = self._estacionamiento[i][j]
                if auto == 0:
                    autos += " 0"
                else:
                    autos += str(auto._patente) + " "
            autos += "\n"
        return autos

e = Estacionamiento(3)   # 3x3
print(e.estaVacio())     # True

print(e.estacionar("AAA111", 8))   # (0,0)
print(e.estacionar("BBB222", 9))   # (0,1)
print(e)                           

print(e.cantidadAutoHora(9))  # autos con horaIngreso < 9 -> 1 (AAA111)
print(e.salir("AAA111"))      # 8
print(e)                      
print(e.estaVacio())          # False (queda BBB222)
print(e.salir("XXX999"))      # None (no existe)
