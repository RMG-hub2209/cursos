print (f'Para conocer la estación del año según el mes en el que estamos: ')
mes = int(input('Introduce el número del mes que deaseas (1-12): '))

estacion = None

if mes == 12 or mes == 1 or mes == 2:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = ' Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'

print (f'Para el mes {mes}, la estación es {estacion}')

