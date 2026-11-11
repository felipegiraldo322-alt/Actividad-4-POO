#Ejercicio 6.7: Validación de campos

class Programador:
    """Modela un integrante de un equipo de programadores."""
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class EquipoMaratónProgramación:
    """Modela un equipo de programadores que participará en una maratón."""
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamaño_equipo = 0
        self.programadores = [None] * 3

    def esta_lleno(self):
        """Determina si el array de programadores está lleno."""
        return self.tamaño_equipo == len(self.programadores)

    def añadir(self, programador):
        """Permite añadir un programador al array si hay espacio."""
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        
        self.programadores[self.tamaño_equipo] = programador
        self.tamaño_equipo += 1

    @staticmethod
    def validar_campo(campo):
        """Valida que el campo no tenga dígitos y su longitud no sea superior a 20 caracteres."""
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")

    @staticmethod
    def main():
        try:
            nombre = input("Nombre del equipo = ")
            universidad = input("Universidad = ")
            lenguaje = input("Lenguaje de programación = ")
            
            equipo = EquipoMaratónProgramación(nombre, universidad, lenguaje)
            
            print("\nDatos de los integrantes del equipo:")
            for i in range(3):
                nombre_programador = input(f"Nombre del integrante {i+1} = ")
                EquipoMaratónProgramación.validar_campo(nombre_programador)
                
                apellidos_programador = input(f"Apellidos del integrante {i+1} = ")
                EquipoMaratónProgramación.validar_campo(apellidos_programador)
                
                programador = Programador(nombre_programador, apellidos_programador)
                equipo.añadir(programador)
            
            print("\n--- ¡Equipo registrado con éxito! ---")
            print(f"Equipo: {equipo.nombre_equipo}")
            print(f"Universidad: {equipo.universidad}")
            print(f"Lenguaje: {equipo.lenguaje_programacion}")
            print("Integrantes:")
            for p in equipo.programadores:
                print(f" - {p}")
                
        except Exception as e:
            print(f"\nExcepción capturada: {e}")


if __name__ == "__main__":
    EquipoMaratónProgramación.main()