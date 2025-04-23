#Nombre
#Año de nacimiento
#Ahora con un cálculo 
#Calcula la edad a partir del año de nacimiento :)
from datetime import datetime

nombre = input("Please tellme your name ")
anoDeNacer = int(input("When were you born? "))
esteAno = datetime.now().year
edad = esteAno - anoDeNacer
print(f"Helo {nombre} you are {edad} years old")