from datetime import datetime

hora = datetime.now().hour
opcionValida = False

while not opcionValida:
    if(hora<12 and hora>4):
        print("Es hora del desayuno te ofrezco las siguientes opiones:")
        print("Pulsa 1 para tosatadas")
        print("Pulsa 2 para cafe con leche")
        print("Pulsa 3 para cereales")
        plato = int(input("cual eliges: "))
        if(plato == 1):
            opcionValida=True
            print("Disfruta de tus tostadas")
        elif(plato == 2):
            opcionValida=True
            print("Disfruta de tu cafe con leche")
        elif(plato == 3):
            opcionValida=True
            print("Disfruta de tus cereales")
        else:
            opcionValida=False
            print("opcion no valida")
    elif(hora<18 and hora>4):
        print("Es hora de la comida te ofrezco las siguientes opiones:")
        print("Pulsa 1 para espaguetis")
        print("Pulsa 2 para pescado al horno")
        print("Pulsa 3 para sopa de verduras")
        plato = int(input("cual eliges: "))
        if(plato == 1):
            opcionValida=True
            print("Disfruta de tus espaguetis")
        elif(plato == 2):
            opcionValida=True
            print("Disfruta de tu pescado al horno")
        elif(plato == 3):
            opcionValida=True
            print("Disfruta de tu sopa de verduras")
        else:
            opcionValida=False
            print("opcion no valida")
    elif(hora<20 and hora>4):
        print("Es hora de la merienda te ofrezco las siguientes opiones:")
        print("Pulsa 1 para sandwich")
        print("Pulsa 2 para barrita energetica")
        print("Pulsa 3 para yogur")
        plato = int(input("cual eliges: "))
        if(plato == 1):
            opcionValida=True
            print("Disfruta de tu sandwich")
        elif(plato == 2):
            opcionValida=True
            print("Disfruta de tu barrita energetica")
        elif(plato == 3):
            opcionValida=True
            print("Disfruta de tu yogur")
        else:
            opcionValida=False
            print("opcion no valida")
    else:
        print("Es hora de la cena te ofrezco las siguientes opiones:")
        print("Pulsa 1 para tortilla")
        print("Pulsa 2 para pizza")
        print("Pulsa 3 para pollo frito")
        plato = int(input("cual eliges: "))
        if(plato == 1):
            opcionValida=True
            print("Disfruta de tu tortilla")
        elif(plato == 2):
            opcionValida=True
            print("Disfruta de tu pizza")
        elif(plato == 3):
            opcionValida=True
            print("Disfruta de tu pollo frito")
        else:
            opcionValida=False
            print("opcion no valida")