print("holii")

deportes=["futbol","Voleibol","Natacion","Basquetbol"]
print(deportes)
print(deportes[2])

#posocion de natacion
pos=deportes.index("Natacion")
print("laposicion de Natacion es:",pos)

#Agregar otro deportes
deportes.append("Hanball")
print(deportes)

#Agregar otro deporte
deportes.append("Tenis")
print(deportes)

cantidad_saludos=int(input("cuantos saludos quieres?"))
for i in range(cantidad_saludos):
    print("hola")

num_deportes=int(input("cuantos deportes agregaras"))
for i in (range(num_deportes)):
  dep=input("ingresa deporte")
  deportes.append(dep)

print(deportes)

    