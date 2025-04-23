inventario = int(input("Cuantos pares de zapatos tenemos? "))
contador = 0
#Prueba de online
print(f"El inventario contiene {inventario} pares de zapatos")
while inventario > 0:
    if inventario <= 10:
        print("ADVERTENCIA: El invertario esta casí vacio.")
    num_zapatos = int(input("Cuantos pares de zapatos quiere el cliente? "))
    if num_zapatos>inventario:
        print(f"No hay suficientes pares de zapatos en stock. Solo quedan {inventario} pares de zapatos")
    else:
        inventario -= num_zapatos
        contador+=1
        print(f"El cliente a pedido {num_zapatos} pares de zapatos. Ahora quedan {inventario} pares de zapatos")
print(f"Hemos hecho {contador} transacciones")
