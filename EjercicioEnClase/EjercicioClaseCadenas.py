
productName = input('Cual es el nombre del producto: ')
productPrice = float(input('Cual es el precio del producto: ').zfill(6))
productStock = float(input('Cuantas unidades se tiene: ').zfill(3))
totalPrice = productStock * productPrice
print(totalPrice)

print('Nombre del Producto', productName,'\n')
print('Precio Unitario', "%09.2f" % productPrice)
print('Numero de unidades', productStock)
print('Precio Toal', "%011.2f" % totalPrice)

# print("%.2f" % productPrice.zfill(6))