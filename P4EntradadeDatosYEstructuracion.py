reticulaDic = {}
decision = '1'
sumaCreditos = 0
formatoGeneral = ''
listaMaterias = ''
while decision == '1':
    print('ciclo')
    materia = input('Ingrese una materia para añadir: ')
    creditos = input('Ingrese los creditos de la materia agregada: ')
    reticulaDic.update({materia: creditos})
    decision = input('Desea ingresar otro registro? \n1-Si \n2-No\n')
print(reticulaDic.items())
for materia, credito in reticulaDic.items():
    formatoGeneral += f'La asignatura: {materia} tiene: {credito} creditos.\n'
    sumaCreditos += int(credito)
    listaMaterias += f'{materia}\n'
print(formatoGeneral)
print(f'El total de creditos de las materias ingresadas fue: {sumaCreditos}\n')
print(f'Lista de materias ingresadas: \n{listaMaterias}')
