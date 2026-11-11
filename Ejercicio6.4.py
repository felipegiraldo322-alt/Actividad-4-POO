#Ejercicio 6.4: Excepciones

class PruebaExcepciones:
    @staticmethod
    def main():
        try:
            print("Ingresando al primer try")
            cociente = 10000 / 0  # Excepción de división por cero
            print("Después de la división")  # Nunca será ejecutada
        except ZeroDivisionError:
            print("División por cero")
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepción
            print("Ingresando al primer finally")

        try:
            print("Ingresando al segundo try")
            objeto = None
            objeto.toString()  # Genera un AttributeError Python
            print("Imprimiendo objeto")  # Nunca será ejecutada
        except ZeroDivisionError:
            print("División por cero")
        except Exception:
            print("Ocurrió una excepción")  # Se captura la excepción general
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepción
            print("Ingresando al segundo finally")

if __name__ == "__main__":
    PruebaExcepciones.main()