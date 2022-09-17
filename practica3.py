while True:
    try:
        estrato=int(input("Estrato?"))
        if estrato<1 or estrato>5:
            print("Estrato debe ser 1 2 3 4")
            continue
        else:
            break
        
    except ValueError:
        print("Debe ser entero")