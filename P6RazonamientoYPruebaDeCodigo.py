#6 Razonamiento y prueba de código - Equipo 4
numero_letras = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez", "Once", "Doce", "Trece", "Catorce", "Quince", "Dieciséis", "Diecisiete", "Dieciocho", "Diecinueve", "Veinte"]
numero = input("Ingrese un número entre el 0 y el 20: ")
print(f"{numero_letras[int(numero)]}" if (int(numero) < 21 and int(numero) >= 0) else "Error, valor ingresado no válido")