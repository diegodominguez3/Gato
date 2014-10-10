print ("                           Juego de Gato                             ")
print (" ")
input("Presione Enter para comenzar")
print ("El Jugador 1 es X")
print ("El jugador 2 es O")
print (" ")
print ("Las X empiezan")
print (" ")
jugador1 = 'Jugador 1'
jugador2 = 'Jugador 2'
juego = 0
board = ["1","2","3","4","5","6","7","8","9"]
def Tablero():
    print (" {}| {}| {}".format(board[0],board[1],board[2]))
    print("---------")
    print (" {}| {}| {}".format(board[3],board[4],board[5]))
    print ("---------")
    print (" {}| {}| {}".format(board[6],board[7],board[8]))
    print(" ")
    return " "


def Ganadorsi(XO):
    if board[0] == XO and board[1] == XO and board[2] == XO:
        return True
    if board[3] == XO and board[4] == XO and board[5] == XO:
        return True
    if board[6] == XO and board[7] == XO and board[8] == XO:
        return True
    if board[0] == XO and board[3] == XO and board[6] == XO:
        return True
    if board[1] == XO and board[4] == XO and board[7] == XO:
        return True
    if board[2] == XO and board[5] == XO and board[8] == XO:
        return True
    if board[0] == XO and board[4] == XO and board[8] == XO:
        return True
    if board[6] == XO and board[4] == XO and board[2] == XO:
        return True
    return False

while (juego == 0):
    jugadas = 0
    turno = 1
    juegoganado = False
    while (jugadas < 9):
        Tablero()
        if turno == 1:
            SigJugada = input("Jugador 1, elige el numero del tablero donde pondras la X: ")
            if board [(int(SigJugada)-1)] == SigJugada:
                board[(int(SigJugada)-1)] = "X"
                if Ganadorsi("X"):
                    juegoganado = True
                    ganador = jugador1
                    break
                turno = 0
                jugadas +=1
            else:
                print ("La jugada que quieres tratar no es valida o ya tomaron ese espacio")
        else:
            SigJugada = input("Jugador 2, elige el numero del tablero donde pondras la O: ")
            if board[(int(SigJugada)-1)] == SigJugada:
                board[(int(SigJugada)-1)] = "O"
                if Ganadorsi("O"):
                    juegoganado = True
                    ganador = jugador2
                    break
                turno = 1
                jugadas +=1
            else:
                print ("La jugada que quieres tratar no es valida o ya tomaron ese espacio")

    if juegoganado == True:
        print (Tablero())
        print("Felicitaciones {} ganaste el juego!".format(ganador))
    else:
        print (" ")
        print("Esto ha sido un empate...")
    break
