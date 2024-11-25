opcion=1
while opcion!=0:
    area1=int(input("ingresa la primer area"))
    area2=int(input("ingresa la segunda area"))
    print("Hola bienvenido al programa")
    print("ingresa 1. area triangulo")
    print("ingresa 2. area rectangulo")
    print("ingresa 3. area circulo")
    print("ingresa 4. convertir temperatura °F a °C")
    print("ingresa 5. convertir temperatura °C a °F")

    op=int(input("¿que operacionqueires realizar"))
    if  (op==1):
        b=int(input("base"))
        h=int(input("altura"))
        res=b*h/2
        print("el area es: ",res)
    elif (op==2):
        b=int(input("base"))
        h=int(input("altura"))
        res=b*h
        print("el area es: ",res)
    elif (op==3):
        r=int(input("radio"))
        res=3.1416*r
        print("el area es:",res)    
    elif (op==4):
        F=int(input("fahrenheit"))
        C=int(input("celsius"))            
        res=C-32*5/9
        print("la temperatura es:",res)
    elif (op==5):
        F=int(input("fahrenheit"))
        res=F*9/5+32
        print("la temperatura es:",res)
    else:
        print("no valido")
    opcion=int(input("deseas continuar, sino prresiona 0. para salir"))

            
