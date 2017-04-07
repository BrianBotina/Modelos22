def lista_digitos(n):
    if n<10:
        return [n]
    else:
        return lista_digitos(n/10)+[n%10]

print(lista_digitos(123))
