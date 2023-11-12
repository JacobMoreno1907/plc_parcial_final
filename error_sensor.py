#https://replit.com/join/emirhilmqw-jacob-olafolaf
Error=0
Contador=0
Veces=int(input("¿Cuántas lecturas de temperatura tienes?: "))
while Contador<Veces:
  Contador+=1
  temperatura=int(input("Inserta la temperatura: "))
  if temperatura>=40 or temperatura<=10:
    Error+=1
porcentaje=(Error/Veces)*100
print("EL sensor se equivocó",Error,"veces")
print("El porcentaje de error del sensor es del",porcentaje,"%.")
