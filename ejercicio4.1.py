presupuesto=100000
print(f"Dispones de 3 gastos de su presuesto de {presupuesto} ")    

for i in range(0,3,1):
    var=input("Desea realisar un gasto -S-  ")
    if var=="S" or var=="s":
        gasto=int(input("De cuanto es \n"))
        presupuesto=presupuesto-gasto
        print(f"El gasto es de  {gasto} y su presupuesto restante es de: {presupuesto}")
    else:
        break

totalPresu=100000-presupuesto
if presupuesto >= 0:
    print(f"Se acabaron los intentos disponibles \n  EL total de sus gastos es de {totalPresu} y el presupuesto restante es de {presupuesto}")
else:
    print(f"El valor de sus gastos es de {totalPresu} excedieron el valor de su presuspuesto, debe al banco: ",presupuesto*(-1) )
