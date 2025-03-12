from tabulate import tabulate

class Producto:
     def __init__(self, nombre, precio, cantidad):
         self.nombre = nombre
         self.precio = precio
         self.cantidad = cantidad
        
inventario = []

for i in range(3):
    print(f"Producto {i + 1}, cual es el nombre?")
    nombre = input()
    print(f"Cual es el precio de '{nombre}'?")
    precio = int(input())
    print(f"Que cantidad hay de '{nombre}'?")
    cantidad = int(input())
    
    producto = Producto(nombre, precio, cantidad)
    inventario.append(producto)
    print("\n")

tabla = [["Producto", "Cantidad", "Precio"]]
for producto in inventario:
    cantidad_str = f"{producto.cantidad} unidades"
    precio_str = f"{producto.precio} pesos"
    tabla.append([producto.nombre, cantidad_str, precio_str])

print("\nResumen:")
print(tabulate(tabla, headers="firstrow", tablefmt="plain"))