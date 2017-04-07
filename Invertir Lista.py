def invertir(lista):
    if lista == []:
        return []
    else:
        return invertir(lista[1:])+[lista[0]]

print(invertir([1,2,3,4,5]))
