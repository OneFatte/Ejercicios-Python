from random import randint

print("APUESTAS")
print("El valor minimo para ingresar es de $100 dolares")
presupuesto=int(input("Con cuanto va a ingresar?  "))
cant=0

if presupuesto >= 100:
    while True:
        apuesta=int(input("Cuanto va a apostar en esta ronda? "))
        eleccion=int(input("Que elige ? solo numeros\n Cara -1-\n Sello -2-"))
        caraSello=randint(1,2)
        cant=cant+1
        
        if (caraSello==1 and eleccion ==1) or (caraSello==2 and eleccion ==2):
            presupuesto=presupuesto+apuesta
            print(f"Sacaste {caraSello}, Ganaste tu total es {presupuesto}")
        elif (caraSello==1 and eleccion ==2) or (caraSello==2 and eleccion ==1):
            presupuesto=presupuesto-apuesta
            print(f"Sacaste {caraSello}, Perdiste tu total es {presupuesto}")
        else:
            print("El valor seleccionado no corresponde")
        
        continuar=input("Desea continuar --S-- --N-- ?  ")
        if continuar=="N" or continuar=="n":
            break
        else:
            continue
    print(f"Ustedde realizo {cant} apuestas \n el total de su dinero es: {presupuesto}")
    
        
        
    
    
    
    
else:
    print("No puede ingresar")