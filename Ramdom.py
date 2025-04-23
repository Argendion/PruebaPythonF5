#Emilio
import random

def juego_adivinanza():
    num_secret= random.randint(1,100)
    tries = 0
    correct = False

    print("Welcome to: GESS THAT NUMBER")
    print("Im thinking of a number between 1 and 100")

    while not correct:
        tryNumber = int(input("try your guess: "))
        tries +=1

        if tryNumber == num_secret:
            correct = True
            print(f"Correct, you got it in {tries} tries")
        elif tryNumber < num_secret:
            print("Wrong, the number is greater")
        else:
            print("Wrong, the number is Smaller")

juego_adivinanza()