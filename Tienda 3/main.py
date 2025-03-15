from tabulate import tabulate

class Producto:
     def __init__(self, nombre, precio, cantidad, desc, clasif):
         self.nombre = nombre
         self.precio = precio
         self.cantidad = cantidad
         self.desc = desc
         self.clasif = clasif
     
     def calcula_precio(self, cantidad):
         return self.precio * cantidad
     
     def inventario_precio(self):
         return self.precio * self.cantidad
        
inventario = []

print("Cuantos productos va a ingresar?")
numero = int(input())

for i in range(numero):
    print(f"Producto {i + 1}, cual es el nombre?")
    nombre = input()
    print(f"Cual es el precio de '{nombre}'?")
    precio = int(input())
    print(f"Que cantidad hay de '{nombre}'?")
    cantidad = int(input())
    print(f"Introduzca la descripción de '{nombre}'?")
    desc = input()
    print(f"Que clasificación tiene '{nombre}'?")
    clasif = input()
    
    producto = Producto(nombre, precio, cantidad, desc, clasif)
    inventario.append(producto)
    print("\n")

tabla = [["Producto", "Cantidad", "Precio", "Descripción", "Clasificación", "Total en inventario", "Precio x5 unidades"]]
for producto in inventario:
    cantidad_str = f"{producto.cantidad} unidades"
    precio_str = f"{producto.precio} pesos"
    descripcion_str = (producto.desc[:10] + "...") if len(producto.desc) > 10 else producto.desc
    total_inventario = f"{producto.inventario_precio()} pesos"
    precio_x5 = f"{producto.calcula_precio(5)} pesos"
    tabla.append([producto.nombre, cantidad_str, precio_str, descripcion_str, producto.clasif, total_inventario, precio_x5])
    
precios_clasificacion = {}
for producto in inventario:
    if producto.clasif in precios_clasificacion:
        precios_clasificacion[producto.clasif] += producto.precio
    else:
        precios_clasificacion[producto.clasif] = producto.precio

tabla_clasificacion = [["Clasificación", "Precio"]]
for clasificacion, total in precios_clasificacion.items():
    tabla_clasificacion.append([clasificacion, f"{total} pesos"])

print("\nResumen:")
print(tabulate(tabla, headers="firstrow", tablefmt="plain"))

print("\nPrecios por clasificación:")
print(tabulate(tabla_clasificacion, headers="firstrow", tablefmt="plain"))
