from random import randint

totalPrecio=0
prodTotal=0
i=0
print("Estamos de aniversario te daremos un descuanto segun tu compra. \n ")

#productos=int(input("Cuantos productos va a registrar ? \n")) #Se piede la cantidad de productos totales

while True:
    i=i+1
    precio=int(input(f"Ingrese el precio del {i} producto ")) #Se pide el precio
    cant=int(input(f"Ingrese la cantidad del {i} producto ")) #Se piede la cantidad de ese producto
    final=input(f" Para finalizar oprima -n- de lo contrario oprima cualquier tecla ")
    prodTotal= precio*cant
    totalPrecio= totalPrecio + prodTotal
    if final=="n" or final=="N":
        break
    else:
        continue

# Aqui se calcula el descuento sobre la compra total
print("La cantidad de productos comprados es de ", i)
if 50000 <= totalPrecio :
    print(f"Aplicas para el descuento el valor de tu compra es {totalPrecio}\n Saca una bolita!\n ")
    bolita=randint(1,4)
    if bolita==1:
        totalPrecio=totalPrecio-(totalPrecio*0.1)
        print(f"Sacaste una bolita  roja, tienes un descuento del 10%. \n Tu valor a pagar es de {totalPrecio}")
    elif bolita==2:
        totalPrecio=totalPrecio-(totalPrecio*0.3)
        print(f"Sacaste una bolita  azul, tienes un descuento del 30%. \n Tu valor a pagar es de {totalPrecio}")
    elif bolita==3:
        totalPrecio=totalPrecio-(totalPrecio*0.5)
        print(f"Sacaste una bolita  amarilla, tienes un descuento del 50%. \n Tu valor a pagar es de {totalPrecio}")
    else :
        totalPrecio=0
        print(f"Sacaste una bolita  blanca, Tu compra es gratis.")
        
else :
    print(f"No aplicas para el descuento, el valor de la compra es de {totalPrecio} necesitas una compra superior a 50.000 COP")

# Devolucion de cambio    
pagar=int(input("Con cuanto desea pagar?"))
cambio=pagar-totalPrecio
print(f"Su cambio es de {cambio}")
