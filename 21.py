import random
def crear_baraja():
    return random.sample([x for x in [2,3,4,5,6,7,8,9,'J','Q','K','A']],12)

def jugar(jugador,casa,maso):
    if len(jugador)<2 and len(casa)<2:
        jugar(jugador+[maso[0]], casa+[maso[1]], maso[2:])
    print(jugador)
    print(casa[:(len(casa)-1)])
    print("LLevas: ",puntosJugador(jugador,0)," puntos")
    if puntosJugador(jugador,0) < 21 and puntosCasa(casa,0) != 21:
        print("La Casa lleva: ",puntosCasa(casa[:len(casa)-1],0)," puntos")
        if input("Deseas continuar? s/n: ") == 's':
            jugar(jugador+[maso[0]], casa+[maso[1]], maso[2:])
            verificar(jugador, casa[:(len(casa)-1)])
        else:
            print("Has plantado en: ",puntosJugador(jugador,0))
            verificar(jugador, casa)
    else:
        verificar(jugador,casa[:len(casa)-1])
        exit()

def verificar(jugador, casa):
    if puntosJugador(jugador,0) == 21:
        print("21, Has ganado!")
        print("Cartas Jugador: ",jugador)
        print("Cartas Casa: ",casa)
        exit()
    if puntosCasa(casa,0) == 21:
        print("Has perdido, la casa llego a 21!")
        print("Cartas Jugador: ",jugador)
        print("Cartas Casa: ",casa)
        exit()
    if puntosJugador(jugador,0) > puntosCasa(casa, 0) and puntosJugador(jugador, 0) < 21:
        print("Felicidades, Has ganado!")
        print("Puntos Casa: ",puntosCasa(casa, 0))
        print("Cartas Jugador: ",jugador)
        print("Cartas Casa: ",casa)
        exit()
    if puntosJugador(jugador,0) < puntosCasa(casa, 0) and puntosCasa(casa, 0) < 21:
        print("Lo siento, has Perdido!")
        print("Puntos Casa: ",puntosCasa(casa, 0))
        print("Cartas Jugador: ",jugador)
        print("Cartas Casa: ",casa)
        exit()
    if puntosCasa(casa, 0) > 21:
        print("Ganaste!, la casa se ha pasado")
        print("Puntos Casa: ",puntosCasa(casa, 0))
        print("Cartas Jugador: ",jugador)
        print("Cartas Casa: ",casa)
        exit()
    if puntosJugador(jugador, 0) > 21:
        print("Perdiste, te has pasado de 21 puntos!")
        print("Puntos Casa: ",puntosJugador(jugador, 0))
        print("Cartas Jugador: ",jugador)
        print("Cartas Casa: ",casa)
        exit()   

def verificarAsJ(jugador):
    if jugador == []:
        return 0
    else:
        if jugador[0] == 'A':
            if input("Tienes un As, Deseas que valga 1 o 11?: ") == '1':
                return 1
            if input("Tienes un As, Deseas que valga 1 o 11?: ") == '11':
                return 11

def verificarAsC(casa):
    if casa == []:
        return 0
    else:
        if casa[0] == 'A':
            if input("Tienes un As, Deseas que valga 1 o 11?: ") == '1':
                return 1
            if input("Tienes un As, Deseas que valga 1 o 11?: ") == '11':
                return 11
            
def puntosJugador(jugador, resultado):
    if jugador == []:
        return resultado
    else:
        if jugador[0] == 'J' or jugador[0] == 'Q' or jugador[0] == 'K':
            return puntosJugador(jugador[1:], resultado+10)
        if jugador[0] == 'A':
            return puntosJugador(jugador[1:],resultado+verificarAsJ(jugador))
        else:
            return puntosJugador(jugador[1:], resultado+jugador[0])
        
def puntosCasa(casa, resultado):
    if casa == []:
        return resultado
    else:
        if casa[0] == 'J' or casa[0] == 'Q' or casa[0] == 'K':
            return puntosCasa(casa[1:], resultado+10)
        if casa[0] == 'A':
            return puntosCasa(casa[1:],resultado+verificarAsC(casa))
        else:
            return puntosCasa(casa[1:], resultado+casa[0])

print(jugar([],[],crear_baraja()))
