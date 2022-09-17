num=int(input("Piensa un numero sumale 5, luego muliplicalo por 3 \n Ingresa el resultado obtenido \n"))
resultado= (num-15)/3

bool=input(f"el numero que penso es: {int(resultado)} ?\n Es correcto SI o NO ?\n")

if bool=="SI" or bool=="Si" or bool=="sI" or bool=="si":
    print("Soy todo un adivino")
else:
    print("Rectifica las cuantas, se que no me equivoco")