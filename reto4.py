from random import randint

seleccion=int(input("Selecciona: \n 1) Piedra \n 2) Papel \n 3) Tijera \n "))

maquina=randint(1,3)

if (seleccion==1 and maquina==3) or (seleccion==2 and maquina==1) or (seleccion==3 and maquina==2) :
    if seleccion==1:
        print(f"Ganaste, sacaste Piedra y la maquina Tijeras")
    elif seleccion==2:
        print(f"Ganaste, sacaste Papel y la maquina Piedra")
    else :
        print(f"Ganaste, sacaste Tijeras y la maquina Papel")     
elif (seleccion==1 and maquina==2) or (seleccion==2 and maquina==3) or (seleccion==3 and maquina==1) :
    if seleccion==1:
        print(f"Perdiste, sacaste Piedra y la maquina Papel")
    elif seleccion==2:
        print(f"Perdiste, sacaste Papel y la maquina Tijeras")
    else :
        print(f"Perdiste, sacaste Tijeras y la maquina Piedra")
else :
    if seleccion==1:
        print(f"Empataste, sacaste Piedra y la maquina Piedra")
    elif seleccion==2:
        print(f"Empataste, sacaste Papel y la maquina Papel")
    else :
        print(f"Empataste, sacaste Tijeras y la maquina Tijeras")
