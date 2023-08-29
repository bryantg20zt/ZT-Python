import datetime
print('Seleccione una opcion para mostrar la fecha del dia de hoy: \n1-YYYY/MM/DD\n2-MM/DD/YYYY')
decision = input()
fechaActual = datetime.datetime.now()

print(fechaActual.strftime('%Y/%m/%d') if decision == '1' else fechaActual.strftime('%m/%d/%Y'))