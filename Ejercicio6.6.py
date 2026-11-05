#Ejercicio 6.6: Catchs multiples

import math

class CalculosNumericos:

    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        try:
            if valor < 0:
                raise ValueError("El valor debe ser un número positivo")
            resultado = math.log(valor)
            print(f"Resultado = {resultado}")
        except ValueError as e:
            if "positivo" in str(e):
                print("El valor debe ser un número positivo para calcular el logaritmo")
            else:
                print("El valor debe ser numérico para calcular el logaritmo")

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        try:
            if valor < 0:
                raise ValueError("El valor debe ser un número positivo")
            resultado = math.sqrt(valor)
            print(f"Resultado = {resultado}")
        except ValueError as e:
            if "positivo" in str(e):
                print("El valor debe ser un número positivo para calcular la raíz cuadrada")
            else:
                print("El valor debe ser numérico para calcular la raíz cuadrada")

if __name__ == "__main__":
    try:
        valor_str = input("Valor numérico = ")
        valor = float(valor_str)
        CalculosNumericos.calcular_logaritmo_neperiano(valor)
        CalculosNumericos.calcular_raiz_cuadrada(valor)
    except ValueError:
        print("El valor ingresado debe ser numérico.")