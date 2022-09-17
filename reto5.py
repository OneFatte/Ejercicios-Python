from random import randint

compra=int(input("Estamos de aniversario te daremos un descuanto segun tu compra. \n 1) De cuanto es tu compra? \n "))

if 50000 <= compra :
    print("Saca una bolita!\n ")
    bolita=randint(1,4)
    if bolita==1:
        total=compra-(compra*0.1)
        print(f"Sacaste una bolita  roja, tienes un descuento del 10%. \n Tu valor a pagar es de {total}")
    elif bolita==2:
        total=compra-(compra*0.3)
        print(f"Sacaste una bolita  azul, tienes un descuento del 30%. \n Tu valor a pagar es de {total}")
    elif bolita==3:
        total=compra-(compra*0.5)
        print(f"Sacaste una bolita  amarilla, tienes un descuento del 50%. \n Tu valor a pagar es de {total}")
    else :
        total=0
        print(f"Sacaste una bolita  blanca, Tu compra es gratis. \n Tu valor a pagar es de {total}")
else :
    print("No aplicas para el descuento, necesitas una compra superior a 50.000 COP")
    

    
    