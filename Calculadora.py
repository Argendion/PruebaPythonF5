number1 = int(input("Inserta el primer numero: "))
number2 = int(input("Inserta el segundo numero: "))
def sum(n1, n2):
    result = n1 + n2
    print(n1, " + ", n2, " = ", result)
def sub(n1, n2):
    result = n1 - n2
    print(n1, " - ", n2, " = ", result)
def mult(n1, n2):
    result = n1 * n2
    print(n1, " * ", n2, " = ", result)
def div(n1, n2):
    if (n1 !=0 and n2 !=0):
        result = n1 / n2
        print(n1, " / ", n2, " = ", result)
    elif(n1==0):
        print("El primer numero es igual a 0 y no se puede calcular")
    else:
        print("El segundo numero es igual a 0 y no se puede calcular")
sum(number1,number2)
sub(number1,number2)
mult(number1,number2)
div(number1,number2)
        
    