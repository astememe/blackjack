from random import shuffle

from Carta import Carta
valores = [1, 2, 3, 4, 5, 6, 7, 10, 10, 10]
nombres = [1, 2, 3, 4, 5, 6, 7, 10, 10, 10]
nombres[0] = "A"
baraja = []
manoJugador = []
manoCrupier = []

def repartir(baraja):
    for i in range (2):
        manoJugador.append(baraja.pop())
        manoCrupier.append(baraja.pop())

def empezarJuego(manoJugador, manoCrupier, baraja):
    suma = 16
    print("Cartas del jugador:")
    for i in range (len(manoJugador)):
         print(f"{manoJugador[i]}")
    print(f"\nCarta inicial del crupier:\n{manoCrupier[0]}")

    if suma >= 16:
        suma = 0
        respuesta = input("Quieres más? S/N")
        if respuesta == "S":
            manoJugador.append(baraja.pop())
            for i in range(len(manoJugador)):
                suma += Carta.getValor(manoJugador[i])
            print("Cartas del jugador:")
            for j in range(len(manoJugador)):
                print(f"{manoJugador[j]}")
            print(f"Tienes suma: {suma.__str__()}")

for i in range(4):
    for j in range(10):
        if j >= 7:
            nombres[7] = "Sota"
            nombres[8] = "Caballo"
            nombres[9] = "Rey"
        if i == 0:
            cartita = Carta("Bastos", valores[j], nombres[j])
            baraja.append(cartita)
        elif i == 1:
            cartita = Carta("Copas", valores[j], nombres[j])
            baraja.append(cartita)
        elif i == 2:
            cartita = Carta("Oros", valores[j], nombres[j])
            baraja.append(cartita)
        else:
            cartita = Carta("Espadas", valores[j], nombres[j])
            baraja.append(cartita)

shuffle(baraja)
repartir(baraja)
empezarJuego(manoJugador, manoCrupier, baraja)


