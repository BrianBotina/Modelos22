import random
def crear_baraja():
    return random.sample([x for x in [2,3,4,5,6,7,8,9,'J','Q','K','A']],12)

def jugar(jugador,mesa,maso):
    if len(jugador)<2 and len(mesa)<2:
        jugar(jugador+[maso[0]], mesa+[maso[1]], maso[2:])
    print(jugador)
    print(mesa[:(len(mesa)-1)])
    if puntosJugador(jugador,0) == 21 and puntosMesa(mesa,0) != 21:
        print("Felicidades, Has ganado!")
        print("Cartas Jugador: ",jugador)
        print("Cartas Mesa: ",mesa)
        exit()
    elif puntosMesa(mesa,0) == 21 and puntosJugador(jugador,0) != 21:
        print("Perdiste, La mesa ha llegado a 21!")
        print("Cartas Jugador: ",jugador)
        print("Cartas Mesa: ",mesa)
        exit()
    elif puntosJugador(jugador,0) > 21:
        print("Lo siento, Has perdido!")
        print("Puntos Jugador: ",puntosJugador(jugador,0))
        print("Cartas Jugador: ",jugador)
        print("Cartas Mesa: ",mesa)
        exit()
    elif puntosMesa(mesa,0) > 21:
        print("La mesa ha perdido, Ganaste!")
        print("Puntos Mesa: ",puntosMesa(mesa,0))
        print("Cartas Jugador: ",jugador)
        print("Cartas Mesa: ",mesa)
        exit()
    if puntosJugador(jugador,0) < 21:
        print("LLevas: ",puntosJugador(jugador,0)," puntos")
        if input("Deseas continuar? s/n: ") == 's':
            jugar(jugador+[maso[0]], mesa+[maso[1]], maso[2:])
        else:
            print("Has plantado en: ",puntosJugador(jugador,0))
            if puntosJugador(jugador,0) > puntosMesa(mesa, 0) and puntosJugador(jugador,0) < 21:
                print("Felicidades, Has ganado!")
                print("Puntos Mesa: ",puntosMesa(mesa, 0))
                print("Cartas Jugador: ",jugador)
                print("Cartas Mesa: ",mesa)
                exit()
            if puntosJugador(jugador,0) < puntosMesa(mesa, 0) and puntosMesa(mesa,0) < 21:
                print("Lo siento, has Perdido!")
                print("Puntos Mesa: ",puntosMesa(mesa, 0))
                print("Cartas Jugador: ",jugador)
                print("Cartas Mesa: ",mesa)
                exit()
            if puntosJugador(jugador,0) == puntosMesa(mesa, 0) and puntosMesa(mesa,0) < 21:
                print("Lo siento, has Perdido!")
                print("Puntos Mesa: ",puntosMesa(mesa, 0))
                print("Cartas Jugador: ",jugador)
                print("Cartas Mesa: ",mesa)
                exit() 

def puntosJugador(jugador, resultado):
    if jugador == []:
        return resultado
    else:
        if jugador[0] == 'J' or jugador[0] == 'Q' or jugador[0] == 'K':
            return puntosJugador(jugador[1:], resultado+10)
        elif jugador[0] == 'A' and resultado >10:
            return puntosJugador(jugador[1:], resultado+1)
        elif jugador[0] == 'A' and resultado <=10:
            return puntosJugador(jugador[1:], resultado+10)
        else:
            return puntosJugador(jugador[1:], resultado+jugador[0])
        
def puntosMesa(mesa, resultado):
    if mesa == []:
        return resultado
    else:
        if mesa[0] == 'J' or mesa[0] == 'Q' or mesa[0] == 'K':
            return puntosMesa(mesa[1:], resultado+10)
        elif mesa[0] == 'A' and resultado >10:
            return puntosMesa(mesa[1:], resultado+1)
        elif mesa[0] == 'A' and resultado <=10:
            return puntosMesa(mesa[1:], resultado+10)
        else:
            return puntosMesa(mesa[1:], resultado+mesa[0])

print(jugar([],[],crear_baraja()))
