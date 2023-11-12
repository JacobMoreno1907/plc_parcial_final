#https://replit.com/join/ptpinanukv-jacob-olafolaf
Clientes=0
Sauco=0
Espino=0
Sauce=0 
Acebo=0
si=0
no=0
Cuantos=int(input("¿Cuantos clientes entraron hoy?: "))
while Clientes<Cuantos:
  Clientes+=1
  compra=str(input("¿El cliente compró algo? (si/no): "))
  if compra =="si":
    si+=1
    varita=str(input(print("¿Que varita compró? 1.Varita de Saúco, 2.Varita de Espino, 3.Varita de Sauce o 4.Varita de Acebo. Elige 1, 2, 3 o 4: ")))
    if varita =="1":
      Sauco+=1
    elif varita =="2":
      Espino+=1
    elif varita =="3":
      Sauce+=1
    elif varita =="4":
      Acebo+=1
  else:
    no+=1
    print("El cliente no compró ninguna varita")
print("Al final del día llegaron ",Cuantos," clientes, si compraron",si," clientes, no compraron",no," clientes, y se vendieron ",Sauco," varitas sauco, ",Espino," varitas espino, ",Sauce," varitas Sauce y ",Acebo," varitas acebo")
print("¡Que gran día para Ollivanders!")
