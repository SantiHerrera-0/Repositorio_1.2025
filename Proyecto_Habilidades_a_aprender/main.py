import csv
import re

#Ingreso_Validacion_Agregado_Habilidad.
def main():
    habilidad = input("Ingresar habilidad nueva: ")
    habilidad = habilidad.strip().lower()
    with open("Habilidades.csv","r+") as archivo:
        lector = [linea.strip() for linea in archivo.readlines()]
        if habilidad in lector:
            print("La habilidad ya esta en la lista.")
        else:
            archivo.write(f"{habilidad}\n") 
main()

