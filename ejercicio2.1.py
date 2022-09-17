leche=input("Trajo la leche? \n Digite s o n \n")
pan=input("Trajo el pan? \n Digite s o n \n")
huevos=input("Trajo los huevos? \n Digite s o n \n")

#Madre estricta
if leche=="s" and pan=="s" and huevos=="s":
    print("Bien hecho \n")
else :
    print("Chanclazo")
    
# Madre comprensiva
if leche=="s" or pan=="s" or huevos=="s":
    print("Bien hecho \n")
else :
    print("Regresese")