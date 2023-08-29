reticulaDic = {}
decision = '1'
sumaCreditos = 0
formatoGeneral = ''
listaMaterias = ''
while decision == '1':
    print('Ingrese una materia para añadir: ')
    materia = input()
    print('Ingrese los creditos de la materia agregada: ')
    creditos = input()
    reticulaDic.update({materia: creditos})
    print('Desea ingresar otro registro? \n1-Si \n2-No')
    decision = input()
print(reticulaDic)
for materia, credito in reticulaDic.items():
    formatoGeneral += f'La asignatura: {materia} tiene: {credito} creditos.\n'
    sumaCreditos += int(creditos)
    listaMaterias += f'{materia}\n'
print(formatoGeneral)
print(f'El total de creditos de las materias ingresadas fue: {sumaCreditos}\n')
print(f'Lista de materias ingresadas: \n{listaMaterias}')
