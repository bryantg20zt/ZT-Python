abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abecedarioFiltered = []

for index, data in enumerate(abecedario):
    if (index % 2) == 0:
        abecedarioFiltered.append(data)


print(abecedarioFiltered)