#Ejercicio 6.8: Lectura de archivos

class LeerArchivo:
    """Tiene como objetivo leer los datos presentes en un archivo de texto con extensión .txt"""

    @staticmethod
    def main():
        # Definición del archivo de texto a leer
        nombre_archivo = "C:/prueba.txt"
        
        try:
            # En Python, 'open' combina las funciones de FileInputStream, InputStreamReader y BufferedReader
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                linea = archivo.readline()
                while linea:
                    # Imprime en pantalla una línea del archivo. 
                    # Se usa end='' porque readline() conserva el salto de línea original.
                    print(linea, end='')
                    linea = archivo.readline()  # Lee la siguiente línea
                    
        except (IOError, FileNotFoundError):
            # En caso de que se genere una excepción (archivo no encontrado o error de lectura)
            print("No se pudo leer el archivo.")

if __name__ == "__main__":
    LeerArchivo.main()