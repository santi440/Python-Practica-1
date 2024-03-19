import random

def descubrir_palabra():
    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    return "".join(letters)

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de fallos permitidos
max_fails = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
while True:
    print("Seleccione la dificultad deseada:")
    dificultad= int(input("""1.Facil \n2.Medio \n3.Dificil\nTu eleccion:"""))

    match dificultad:
        case 1:
            print("Seleccionaste dificultad Facil")
            guessed_letters.extend(["a","e","i","o","u","á","é","í","ó","ú"])
            break
        case 2:
            print("Seleccionaste dificultad Media")
            guessed_letters.extend([secret_word[0],secret_word[-1]])
            break
        case 3:
            print("Seleccionaste dificultad DIFICIL")
            break
        case _:
            print("Seleccion no valida. Por favor ingrese un numero entre 1 y 3")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed=descubrir_palabra()

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

while max_fails<10:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Verificar si la letra ya ha sido adivinada o es vacio
    if (letter == ""):
        print("Por favor ingrese una letra")
        continue
    elif letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    
    
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        max_fails+=1
    
    # Mostrar la palabra parcialmente adivinada
    word_displayed=descubrir_palabra()
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado tus {max_fails} errores.")
    print(f"La palabra secreta era: {secret_word}")
