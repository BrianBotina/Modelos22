
def ordenarA(lista):
    return ordenarA((list(filter(lambda x: x if (x[0]=='a' or x[0]=='A') else [],lista)))+ordenarB(lista))
def ordenarB(lista):
    return list(filter(lambda x: x if (x[0]=='b' or x[0]=='B') else [],lista))+ordenarC(lista)
def ordenarC(lista):
    return list(filter(lambda x: x if (x[0]=='c' or x[0]=='C') else [],lista))+ordenarD(lista)
def ordenarD(lista):
    return list(filter(lambda x: x if (x[0]=='d' or x[0]=='D') else [],lista))+ordenarE(lista)
def ordenarE(lista):
    return list(filter(lambda x: x if (x[0]=='e' or x[0]=='E') else [],lista))+ordenarF(lista)
def ordenarF(lista):
    return list(filter(lambda x: x if (x[0]=='f' or x[0]=='F') else [],lista))+ordenarG(lista)
def ordenarG(lista):
    return list(filter(lambda x: x if (x[0]=='g' or x[0]=='G') else [],lista))+ordenarH(lista)
def ordenarH(lista):
    return list(filter(lambda x: x if (x[0]=='h' or x[0]=='H') else [],lista))+ordenarI(lista)
def ordenarI(lista):
    return list(filter(lambda x: x if (x[0]=='i' or x[0]=='I') else [],lista))+ordenarJ(lista)
def ordenarJ(lista):
    return list(filter(lambda x: x if (x[0]=='j' or x[0]=='J') else [],lista))+ordenarK(lista)
def ordenarK(lista):
    return list(filter(lambda x: x if (x[0]=='k' or x[0]=='K') else [],lista))+ordenarL(lista)
def ordenarL(lista):
    return list(filter(lambda x: x if (x[0]=='l' or x[0]=='L') else [],lista))+ordenarM(lista)
def ordenarM(lista):
    return list(filter(lambda x: x if (x[0]=='m' or x[0]=='M') else [],lista))+ordenarN(lista)
def ordenarN(lista):
    return list(filter(lambda x: x if (x[0]=='n' or x[0]=='N') else [],lista))+ordenarÑ(lista)
def ordenarÑ(lista):
    return list(filter(lambda x: x if (x[0]=='ñ' or x[0]=='Ñ') else [],lista))+ordenarO(lista)
def ordenarO(lista):
    return list(filter(lambda x: x if (x[0]=='o' or x[0]=='O') else [],lista))+ordenarP(lista)
def ordenarP(lista):
    return list(filter(lambda x: x if (x[0]=='p' or x[0]=='P') else [],lista))+ordenarQ(lista)
def ordenarQ(lista):
    return list(filter(lambda x: x if (x[0]=='q' or x[0]=='Q') else [],lista))+ordenarR(lista)
def ordenarR(lista):
    return list(filter(lambda x: x if (x[0]=='r' or x[0]=='R') else [],lista))+ordenarS(lista)
def ordenarS(lista):
    return list(filter(lambda x: x if (x[0]=='s' or x[0]=='S') else [],lista))+ordenarT(lista)
def ordenarT(lista):
    return list(filter(lambda x: x if (x[0]=='t' or x[0]=='T') else [],lista))+ordenarU(lista)
def ordenarU(lista):
    return list(filter(lambda x: x if (x[0]=='u' or x[0]=='U') else [],lista))+ordenarV(lista)
def ordenarV(lista):
    return list(filter(lambda x: x if (x[0]=='v' or x[0]=='V') else [],lista))+ordenarW(lista)
def ordenarW(lista):
    return list(filter(lambda x: x if (x[0]=='w' or x[0]=='W') else [],lista))+ordenarX(lista)
def ordenarX(lista):
    return list(filter(lambda x: x if (x[0]=='x' or x[0]=='X') else [],lista))+ordenarY(lista)
def ordenarY(lista):
    return list(filter(lambda x: x if (x[0]=='y' or x[0]=='Y') else [],lista))+ordenarZ(lista)
def ordenarZ(lista):
    return list(filter(lambda x: x if (x[0]=='z' or x[0]=='Z') else [],lista))


def ordenar_lista(lista):
        return sorted(lista)
def ordenar(lista):
    if lista == []:
        return []
    if lista[0][0] == 'a':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'b':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'c':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'd':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'e':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'f':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'g':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'h':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'i':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'j':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'k':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'l':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'm':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'n':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'ñ':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'o':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'p':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'q':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'r':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 's':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 't':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'u':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'v':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'w':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'x':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'y':
        return [lista[0]]+ordenar(lista[1:])
    if lista[0][0] == 'z':
        return [lista[0]]+ordenar(lista[1:])
    else:
        return ordenar(lista[1:])

print(ordenarA(["asdasd","cvbcvb","awrer","asqw","basder","zxcasd","fghfgh","mkjk","asvdasd"]))
print(ordenar_lista(["asdasd","cvbcvb","awrer","asqw","basder","zxcasd","fghfgh","mkjk"]))
print(ordenar(["asdasd","cvbcvb","awrer","asqw","basder"]))
