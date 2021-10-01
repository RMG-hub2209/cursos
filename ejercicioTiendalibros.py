tituloLibro = input('Ingrese el Título del libro: ')
idLibro = int(input('Ingrese el Id del libro: '))
precioLibro = float(input('Ingrese el precio del libro: '))
envioLibro = input('¿El envio fue gratis? (True/False): ')

if envioLibro == 'True':
    envioLibro = True
elif envioLibro == 'False':
    envioLibro = False
else:
    envioLibro = input('Dato incorrecto, debe indicar si es True/False: ')

print (f'''
   Titulo: {tituloLibro}
   ID: {idLibro}
   Precio: {precioLibro}
   Envio: {envioLibro}
''')
