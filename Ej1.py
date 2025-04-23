##Declarar bariables
##nombre = input("¿Cual es tu nombre? ")
edad = int(input("¿Cual es tu edad? "))
##print(f"Hola {nombre}! Tienes {edad} años")

##def saludar(n):
  ##  print(f"Hola {n}, bienvenid@ al taller")
##saludar(nombre)

##for recorrer in range(1,10):
  ##  print(recorrer)

def esMayorDeEdad(e):
    if e >= 18:
        return "Eres mayor de edad."
    else:
        return "Eres menor de edad."
print(esMayorDeEdad(edad))