presupuesto=100000
cant=int(input(f"Dispones de 3 gastos de su presuesto de {presupuesto} cuantos desea realizar? "))
cont=0
if cant>=1 and cant<=3:
    for i in range(0,cant,1):
        gasto=int(input("De cuanto es \n"))
        presupuesto=presupuesto-gasto
        if presupuesto >= 0:
            print(f"El gasto es de  {gasto} y su presupuesto restante es de: {presupuesto}")
        else:
            print("No se puede continuar con el gasto, excedio su presupuesto")
            presupuesto=presupuesto+gasto
            break
else:
    print("Solo se permite 3 intentos")
totalPresu=100000-presupuesto
print(f"Se acabaron los intentos disponibles \n  EL total de sus gastos es de {totalPresu} y el presupuesto restante es de {presupuesto}")
