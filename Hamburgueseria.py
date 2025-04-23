inventario = 100
#Prueba de online
print(f"El inventario contiene {inventario} hamburguesas")
while inventario > 0:
    if inventario <= 10:
        print("ADVERTENCIA: El invertario esta casí vacio.")
    num_hamburguesas = int(input("Cuantas hamburguesas quiere el cliente?"))
    if num_hamburguesas>inventario:
        print(f"No hay suficientes hamburguesas en stock. Solo quedan {inventario} hamburguesas")
    else:
        inventario -= num_hamburguesas
        print(f"El cliente a pedido{num_hamburguesas} hamburguesas. Ahora quedan {inventario} hamburguesas")

