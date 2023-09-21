palabra = input("Ingrese una palabra a buscar en el texto: \n")
with open("ref.txt", "r", encoding="utf-8") as text:
    words = text.read().split(" ")
    repits = 0
    characters = 1
    aparitionArray = []
    for index, word in enumerate(words):
        if word.lower() == palabra.lower():
            aparitionArray.append(characters)
            repits += 1
        characters += len(word) + 1
print({"Apariciones": repits, "Posiciones de aparacion": aparitionArray})
