prom=0
cont=0
while True:
    for i in range(1,5,1):
        nota=float(input("Digite su nota valor de 1.0 a 5.0 \n"))
        if nota<1:
            print("Nota debe ser mayor o igual que 1\n reinicie el programa")
            prom=0
            cont=0
            break
        else:
            prom=prom+nota
            cont=cont+1
            continue
    notaFinal=prom/cont
    if notaFinal>=1 and notaFinal<3:
        print(f"Reporbaste la asignatura, sacaste= {notaFinal}\n")
    elif notaFinal>=3 and notaFinal<=4:
        print(f"Pasaste raspando la asignatura, sacaste= {notaFinal}\n")
    elif notaFinal>4:
        print(f"Aprobaste con buenos resultado, sacaste= {notaFinal}\n")
    else:
        print("Error")
        
    var=input("Revisar otro estudiante -S- \n Terminar -N-")
    if var=="S" or var=="s":
        cont=0
        prom=0
        continue
    else:
        break