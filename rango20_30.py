rangoEdad = int(input("Introduce tu edad: "))
#veintes = rangoEdad >= 20 and rangoEdad < 30
#treintas = rangoEdad >=30 and rangoEdad < 40

#if veintes or treintas:
#    if veintes:
#        print('Estas dentro del rango de los 20\'s')
#    elif treintas:
#        print('Estás dentro del rango de los 30\'s')

#else: 
#    print('No estás dentro del rango')

#####Usualmente el valor de las variables va dentro de la función "if" por lo que debería ser
#####escrito de la siguiente manera
if (rangoEdad >= 20 and rangoEdad < 30) or (rangoEdad >=30 and rangoEdad < 40):
    print('Estás dentro de los 20\'s o treintas\'s')
else:
    print('Estás fuera del rango')

###Sin embargo, se pierde la oportunidad de hacer preguntas más exactas que con los if's anidados