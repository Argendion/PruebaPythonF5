import statistics as sttt #Funciones para calculos estadisticos
import numpy as np #Para operaciones matematicas avanzadas -> Arrays

zanahorias = [300, 280, 290, 310, 275, 290, 295, 315, 290, 280, 310, 305]
import matplotlib.pyplot as plt #Hacer estadisticas
condition= True

while condition:
  print("Analisis de la cosecha")
  media = np.mean(zanahorias) #Promedio
  print(f"la media es: {media}g")
  mediana = np.median(zanahorias) #Valor centra
  print(f"la media es: {mediana}g")
  moda = sttt.mode(zanahorias) #El valor mas frecuente
  print(f"la moda es: {moda}g")
  desviacion = np.std(zanahorias) #Desviacion estandar
  print(f"la desviacion es: {desviacion:.2f}g")
  plt.hist(zanahorias)
  plt.show()
  con = input("Quieres añadir valor? S/N: ")
  if con == "S":
    zanahorias.append(int(input("Ingrese la cantidad de zanahoria: ")))
  else:
    condition = False