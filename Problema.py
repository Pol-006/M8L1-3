from PIL import Image
import random

    Ejemlos = {
    "Charizard": "Menos árboles para absorber CO₂, agravando el calentamiento global.",
    "Pikachu": "Emisión de metano y óxido nitroso por ganado y fertilizantes."
}
print("Algunos pokemones son mejores que otros por sus estadisticas, por los movimenitos que puede aprender")
print("por su habilidad o por su combinacion con un objeto.")
print("Por cualquiera de estas razones es que usar tu pokemon favorito en competitivo no sea la mejor idea")
print("pero realmente al integrarlo solo estas perdiendo la oportunidad de poner un pokemon ")
print("que cumple la misma función pero mejor")

print("¿Quieres saber algunos ejemplos? Elige una de estas palabras (escribelas exactamente igual): Charizard o Pikachu")
word = input("Escribe uno de los 2 pokemones: ")

if word in Ejemlos.keys():
    print(Ejemlos[word])
else:
    print("Este pokemon no está en la lista")

    # Rutas a imagenes
Imagenes = [
    "c:/Escritorio/popi/Charizard.png",
    "c:/Escritorio/popi/Pikachu.png"
    
]

# Imagen aleatoria
imagen_seleccionada = random.choice(Imagenes)
imagen = Image.open(imagen_seleccionada)
imagen.show()
