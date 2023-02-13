#Respoder correctamente o se acaba el juego.

print("Responde correctamente a las siguientes preguntas, de lo contrario acaba el juego (si o no en minúscula)")

pregun1 = input("¿Colón descubrió América?")

if pregun1 == "si":
    pregun2 = input("¿La independencia de Colombia fue en 1810?")
    if pregun2 == "si":
        pregun3 = input("¿The Doors fue un grupo de rock Americano?")
        if pregun3 == "si":
            print("¡Ganaste el genio, maldito juego!") 
        else:
            print("fin del juego")
    else:
        print("fin del juego")
else:
    print("fin del juego")

    

