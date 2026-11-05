#Ejercicio 6.4: Excepciones

class PruebaExcepciones:
    @staticmethod
    def main():
        # Primer bloque try
        try:
            print("Ingresando al primer try")
            cociente = 10000 / 0  # Se lanza una excepción de división por cero
            print("Después de la división")  # Esta instrucción nunca será ejecutada
        except ZeroDivisionError:
            print("División por cero")  # Se imprime en pantalla este mensaje
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepción
            print("Ingresando al primer finally")

        # Segundo bloque try
        try:
            print("Ingresando al segundo try")
            objeto = None
            objeto.toString()  # Se lanza una excepción (en Python genera AttributeError)
            print("Imprimiendo objeto")  # Esta instrucción nunca será ejecutada
        except ZeroDivisionError:
            print("División por cero")
        except Exception:
            print("Ocurrió una excepción")  # Se captura la excepción general
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepción
            print("Ingresando al segundo finally")

if __name__ == "__main__":
    PruebaExcepciones.main()