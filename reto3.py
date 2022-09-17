from random import randint
print("Para ganar necesitas pares de 1 o 6 \n o una suma ganadora de 3, 7 o 11 \n ")


dado1=randint(1,6)
dado2=randint(1,6)

suma=dado1+dado2

if (dado1==1 and dado2==1) or (dado1==6 and dado2==6):
    print(f"Ganastes, sacaste pares en \n Dado1: {dado1} y en Dado2: {dado2} \n")
elif suma==3 or suma==11 or suma==7:
    print(f"Ganastes, sacaste una suma ganadora en \n Dado1: {dado1} y en Dado2: {dado2} \n")
else:
    print(f"Perdiste, no sacaste una suma ganadora o pares en \n Dado1: {dado1} y en Dado2: {dado2} \n")
