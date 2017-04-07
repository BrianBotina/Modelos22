def menores(lista):
    if lista == []:
        return []
    else:
        return [menor(lista[0])]+menores(lista[1:])

def menor(lista):
    return min(lista)
print(menores([[1,2,3,4,5],[6,7,8,9],[23,90,50,11]]))
