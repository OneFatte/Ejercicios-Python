print("El centro de salud Famisalud, aplica vacunas a los bebes menores de un año")

edad=int(input("Ingrese la edad en meses"))
peso=int(input("Ingrese el peso del bebe"))

dosis=((peso+10)/(edad*10))*8

print(f"la dosis a aplicar al bebe es de {dosis}")