prom=0
cont=0
for i in range(1,5,1):
    nota=float(input("Digite su nota valor de 1.0 a 5.0 \n"))
    prom=prom+nota
    cont=cont+1
    
notaFinal=prom/cont

if notaFinal<3:
    print(f"Reporbaste la asignatura, sacaste= {notaFinal}")
elif notaFinal>=3 and notaFinal<=4:
    print(f"Pasaste raspando la asignatura, sacaste= {notaFinal}")
elif notaFinal>4:
    print(f"Aprobaste con buenos resultado, sacaste= {notaFinal}")
else:
    print("Debe ser float")