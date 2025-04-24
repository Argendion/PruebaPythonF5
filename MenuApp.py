opcionValida = bool(False)

introList = ["pantera[]", "felinae[]", 1]

pantera = ["Leon[]", "Jaguar[]", "Tigre[]", 2]
felinae = ["BlackFooted[]","ComunEuropeo[]","Jungla[]", 2]
OtherCats = ["RustSpot[]", "Pallas[]", 2]

Leon=["Panthera leo", "Africa y India", "Unica pantera que caza en grupo"]
Tigre=["Panthera tigris", "Asia", "El felino más grande"]
Jaguar=["Panthera onca", "Las Americas", "Mayor mordedura en proporcion a peso"]
BlackFooted=["Felis nigripies", "Africa", "Los adultos mas grandes llegan al los 52 cm de cabeza a cola"]
ComunEuropeo=["Felis catus", "Todo el mundo", "El tercer animal que mas especies a extinguido"]
Jungla=["Felis chaus", "Mediterraneo Este y Sur y centro sur asia", "El gato pequeño más grande"]


#Dar opciones a elegir
def OpionesAElegir(o1):
    print("Sobre que quieres aprender?")
    for counter in range(1, len(o1)):
        print(f" {o1[counter-1]}")
    curiosity = input("elije ")
    ChechIfValid(o1,curiosity)


#Confirma que selecction es valida
def ChechIfValid(c1,a1):
    if a1 in c1:
        if 1 in c1:
            """
            for recorrer in range(1,len(c1)):
                if a1 == "Leon":
                    OpionesAElegir(Leon)
                if a1 == "Tigre":
                    OpionesAElegir(Tigre)
                if a1 == "Jaguar":
                    OpionesAElegir(Jaguar)
                if a1 == "BlackFooted":
                    OpionesAElegir(BlackFooted)
                if a1 == "ComunEuropeo":
                    OpionesAElegir(ComunEuropeo)
                if a1 == "Jungla":
                    OpionesAElegir(Jungla)
                """
            OpionesAElegir(exec(a1))
        else:
            Info(exec(a1))          
    else:
        print("Opcion invalida")
        OpionesAElegir(c1)

#Extraer informacion
def Info(i1):
    print(f"El nombre cientifico es: {i1[0]}")
    print(f"Esta animal vive en: {i1[1]}")
    print(f"Una curiosidad es: {i1[2]}")
    OpionesAElegir(introList)

OpionesAElegir(introList)
    