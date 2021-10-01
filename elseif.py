condicion = input('True or False: ')

if condicion == 'True':
    condicion = True
    print ('La condicion es Verdadera')
elif condicion == 'False':
    condicion = False
    print ('La condicion es Falsa')
else:
    print ('Parámetro no válido')
    condicion = input('Ingresa un parámetro válido (True/False): ')

print (f'Fin del programa')