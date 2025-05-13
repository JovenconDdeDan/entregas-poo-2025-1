class Matriz:
    def __init__(self, valores):
        self.valores = valores  # Lista de listas de matrices 2x2

    def __add__(self, otra):
        return Matriz([
            [self.valores[0][0] + otra.valores[0][0], self.valores[0][1] + otra.valores[0][1]],
            [self.valores[1][0] + otra.valores[1][0], self.valores[1][1] + otra.valores[1][1]]
        ])

    def __sub__(self, otra):
        return Matriz([
            [self.valores[0][0] - otra.valores[0][0], self.valores[0][1] - otra.valores[0][1]],
            [self.valores[1][0] - otra.valores[1][0], self.valores[1][1] - otra.valores[1][1]]
        ])

    def __mul__(self, otra):
        a, b = self.valores, otra.valores
        return Matriz([
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ])

    def mostrar(self):
        print(f"|{self.valores[0][0]}  {self.valores[0][1]}|")
        print(f"|{self.valores[1][0]}  {self.valores[1][1]}|")

def leer_matriz(numero):
    print(f"> Matriz {numero}: elemento 0,0")
    a = int(input("< "))
    print(f"> Matriz {numero}: elemento 0,1")
    b = int(input("< "))
    print(f"> Matriz {numero}: elemento 1,0")
    c = int(input("< "))
    print(f"> Matriz {numero}: elemento 1,1")
    d = int(input("< "))
    return Matriz([[a, b], [c, d]])

def main():
    matriz1 = leer_matriz(1)
    matriz2 = leer_matriz(2)

    print("> Matriz 1:")
    matriz1.mostrar()
    print("> Matriz 2:")
    matriz2.mostrar()

    print("> Escriba 1 para suma,\n>         2 para resta,\n>         3 para multiplicación")
    opcion = int(input("< "))

    if opcion == 1:
        resultado = matriz1 + matriz2
        print("> La suma de las dos matrices es:")
    elif opcion == 2:
        resultado = matriz1 - matriz2
        print("> La resta de las dos matrices es:")
    elif opcion == 3:
        resultado = matriz1 * matriz2
        print("> El producto de las dos matrices es:")
    else:
        print("> Opción inválida.")
        return

    resultado.mostrar()

if __name__ == "__main__":
    main()
