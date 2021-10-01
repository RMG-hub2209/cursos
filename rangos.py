numero = int(input("Ingresa un número: "))
numeroMaximo=5
numeroMinimo=0

dentroRango = (numero >= numeroMinimo) and (numero <=numeroMaximo)

if dentroRango:
    print(f'El numero {numero} está dentro del rango')
else:
    print(f'El numero {numero} no está dentro del rango')

print ("Fin del programa")