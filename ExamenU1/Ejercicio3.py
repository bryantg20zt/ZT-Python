class Location:
  nombre = ''
  porcentajeIVA = 0.0
  items = []

  def sumaItems (self):
    sumatoriaTotal = 0
    for item in self.items:
      print(sumatoriaTotal)
      print("Suma: ", item.precio, item.cantidad)
      sumatoriaTotal = sumatoriaTotal + (item.precio * item.cantidad)
    sumatoriaTotal = sumatoriaTotal + ((self.porcentajeIVA / 100) * sumatoriaTotal)
    print("----------------------")
    print("La sumatoria total es de: ", sumatoriaTotal)
    

class Item: 
  nombre = ''
  cantidad = 0
  precio = 0


flagToCapture = True
locacionData = Location()

locacionData.nombre = input("Nombre de la locacion: ")
locacionData.porcentajeIVA = int(input("Ingrese el porcentaje de la locacion: "))
print("----------CAPTURAR ITEMS-----------")
while flagToCapture:
  itemToAdd = Item()
  print(len(locacionData.items))
  if len(locacionData.items) == 0:
    itemToAdd.nombre = input("Ingrese el nombre del Item a agregar: ")
    itemToAdd.cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    itemToAdd.precio = precio
    locacionData.items.append(itemToAdd)
  else:
    nombreItem = input("Ingrese el nombre del item: ")
    for locationItem in locacionData.items:
      if nombreItem == locationItem.nombre:
        print("Item ya existente :(")
    else:
      itemToAdd.cantidad = int(input("Ingrese la cantidad: "))
      itemToAdd.precio = float(input("Ingrese el precio: "))
      locacionData.items.append(itemToAdd)
  print("------------------------------------")
  optionUserSelected = int(input("Desea agregar otro item? \n(1) SI \n(2) NO "))
  if optionUserSelected == 2:
    locacionData.sumaItems()
    flagToCapture = False

