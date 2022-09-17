
edad=int(input(" Bienvenido a PLAYLAND \n Cual es su edad ? \n"))

if 0 <= edad <= 4:
    print(f"El valor de la entrada del niño es gratis")
elif 4 < edad <=18:
    print(f"El valor de la entrada del joven es de 20'000 COP")
elif 18 < edad <= 65:
    print(f"El valor de la entrada del aduldo es de 15'000 COP") 
elif 65 < edad: 
    print(f"El valor de la entrada del señor es de 3'000 COP")
else :
    print(f"La edad ingresada es incorrecta !")

