import numpy as np

with open("csv1.csv") as file_name:
  array = np.genfromtxt(file_name, delimiter=",", dtype=None, names=True)

# print(array)
# print(spamreader)


indexRow = ''
productsReviews = []
arrayToConvertCSV = []

def validateExists (row):
  if len(productsReviews) > 0:
    for rowSearch in productsReviews:
      if row[0] == rowSearch[1] and row[1] == rowSearch[1] and row[2] == rowSearch[2]:
        return True
  else:
    return False

for row in array:
  indexRow = row
  for rowSearching in array:
    if not validateExists(rowSearching):
      if indexRow[0] == rowSearching[0] and (indexRow[1] != rowSearching[1] or indexRow[2] != rowSearching[2]):
        print("Existen dos iguales con cambios")
        print("opcion 1: " , indexRow)
        print("opcion 2: " , rowSearching)
        userInput = int(input(""))
        if(userInput == 1):
          productsReviews.append(rowSearching)
          print("Agregando opcion 1")
          arrayToConvertCSV.append(rowSearching)
        else:
          print("Agregando opcion 2")
          productsReviews.append(rowSearching)
          arrayToConvertCSV.append(rowSearching)
  arrayToConvertCSV.append(row)


print(arrayToConvertCSV)
np.savetxt('nuevo.csv', arrayToConvertCSV, delimiter=",")