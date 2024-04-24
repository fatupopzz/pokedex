import csv
import os
import csv


#preguntar al ususario si que pokemon quiere buscar

def buscar_pokemon(number):
    with open('pokemon.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == str(number):  
                return row
    return None
   

while True:
    number = input("Ingrese el número del Pokémon que desea buscar (o 'q' para salir): ")   
    pokemon = buscar_pokemon(number)
    if pokemon:
        print("El Pokémon encontrado es:", pokemon[1], "y es de tipo", pokemon[2])
    else:
        print("No se encontró ningún Pokémon con ese número.")
