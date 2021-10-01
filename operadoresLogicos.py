#Operador and
diaDescanso = False
diaVacaciones = True

#if diaVacaciones and diaDescanso:
#    print("Puedo asistir al juego")
#else:
#    print("No puedo, tengo trabajo")


#Operador or
#if diaVacaciones or diaDescanso:
#    print("Puedo asistir al juego")
#else:
#   print("No puedo, tengo trabajo") 


#operador not
if not(diaDescanso and diaVacaciones):
    print("No puedo, tengo trabajo")
else:
    print("Puedo ir al juego")