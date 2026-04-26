from proyecto_matrices import operaciones_matrices as om
from proyecto_matrices import entrada as ent
def mostrar_menu():
  opcion = 0
  while opcion != 5:
    print("-MENU DE OPERACIONES CON MATRICES- \n 1) Suma de matrices \n 2) Multiplicación de matrices \n 3) Producto Hadamard \n 4) Producto Kronecker \n 5) Salir")
    try:
      opcion = int(input("Seleccione una opcion: "))
      opciones = [1, 2, 3, 4]
      if opcion in opciones:
        ent.resultado(opcion)
        continue
      elif opcion == 5:
        return "Hasta luego :)"
      else:
        print("Opción no válida")
        continue
    except ValueError:
      print("Error: Debes digitar un numero")
