#Ejercicio 6.8: Lectura de archivos

class LeerArchivo:
    """Tiene como objetivo leer los datos presentes en un archivo de texto con extensión .txt"""

    @staticmethod
    def main():
        nombre_archivo = "Linea 1.txt"
        
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                linea = archivo.readline()
                while linea:
                    print(linea, end='')
                    linea = archivo.readline()
                    
        except (IOError, FileNotFoundError):
            # En caso de que se genere una excepción
            print("No se pudo leer el archivo.")

if __name__ == "__main__":
    LeerArchivo.main()