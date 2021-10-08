edad = int(input('Introduce tu edad: '))
etapaVida = ''

if edad <= 10:
    etapaVida = 'La infancia es increible'
    print (etapaVida)
elif edad >= 11 and edad <= 20:
    etapaVida = 'Muchos cambios y mucho estudio'
    print (etapaVida)
elif edad >= 21 and edad <= 30:
    etapaVida = 'Amor y comienza el trabajo'
    print (etapaVida)
else:
    etapaVida = 'Etapa no considerada'
    print (etapaVida)

print (f'Fin del programa')