for i in range(10):
    numero=int(input("Escriba un numero "))
    if numero != 0:
        valor= numero % 2
        if valor==0:
            print(f"El numero {numero} es positivo")
        else:
            print(f"El numero {numero} es negativo")
    else:
        print(f"El numero {numero} es neutro")

