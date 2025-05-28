from datetime import datetime

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def get_datos(self):
        return {
            'Clase': self.__class__.__name__,
            'Nombre': self.nombre,
            'Edad': f"{self.edad} años",
            'Raza': self.raza,
            'Fecha de ingreso': self.fecha_ingreso
        }

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

def main():
    mascotas = []
    cantidad = int(input("Cuantas mascotas va a ingresar?\n"))

    for i in range(1, cantidad + 1):
        tipo = input(f"Mascota {i}, que clase es (P)erro o (G)ato?\n").strip().lower()

        while tipo not in ['p', 'g', 'perro', 'gato']:
            tipo = input("Entrada inválida. Ingrese (P)erro o (G)ato:\n").strip().lower()

        clase = Perro if tipo.startswith('p') else Gato
        clase_nombre = "Perro" if clase == Perro else "Gato"

        nombre = input(f"cual es el nombre del {clase_nombre}?\n").strip().capitalize()
        edad = int(input(f"que edad tiene '{nombre}'?\n"))
        raza = input(f"de que raza es '{nombre}'?\n").strip().capitalize()

        mascota = clase(nombre, edad, raza)
        mascotas.append(mascota)

    print("> Resumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    for m in mascotas:
        datos = m.get_datos()
        print(f"|{datos['Clase']:<6}|{datos['Nombre']:<9}|{datos['Edad']:<7}|{datos['Raza']:<13}|{datos['Fecha de ingreso']}|")

if __name__ == "__main__":
    main()