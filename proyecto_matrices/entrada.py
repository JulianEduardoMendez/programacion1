from proyecto_matrices import operaciones_matrices as om
from proyecto_matrices import entrada as ent
def ingresar_matriz():
  while True:
    b = input("Ingrese las filas separadas por ';': ").split(";")
    matriz = []
    value = True
    try:
      for i in range(len(b)):
        c = b[i].split()
        if len(c) == 0:
          print("Error: debes digitar algun numero")
          value = False
          break
        else:
          a = list(map(float,c))
          matriz.append(a)
      if value == False:
        continue

      for j in range(len(matriz)):
        if len(matriz[j]) != len(matriz[0]):
          value = False
          break
      if value == True:
        return matriz
      else:
        print("Error: La cantidad de columnas debe ser igual para todas las filas")
    except ValueError:
      print("Error: Debes poner numeros")

def resultado(a):
  matriz01 = ent.ingresar_matriz()
  matriz02 = ent.ingresar_matriz()
  if a == 1:
    resultado1 = om.suma(matriz01, matriz02)
    return resultado1
  elif a == 2:
    resultado2 = om.multiplicacion(matriz01, matriz02)
    return resultado2
  elif a == 3:
    resultado3 = om.p_h(matriz01, matriz02)
    return resultado3
  elif a == 4:
    resultado4 = om.p_k(matriz01, matriz02)
    return resultado4
