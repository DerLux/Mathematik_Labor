import matplotlib.pyplot as plt
import numpy as npy
import math as m


print("Authors: Tobias Stöhr, Lukas Butscher, Wiebke Prinz, Jona Böcker\n")

TOL = 1e-12  # Abbruchbedingung
f = lambda y: 1 / 3 * m.sqrt((100 - y) ** 2 + 100 ** 2) + 1 / 5 * m.sqrt(100 ** 2 + y ** 2)  # Funktion
Df = lambda y: ((y - 100) / (3 * m.sqrt((100 - y) ** 2 + 100 ** 2))) + y / (5 * m.sqrt(100 ** 2 + y ** 2))  # Abl
# DDf = lambda y: 1 / (5 * m.sqrt(y ** 2 + 10000)) - y ** 2 / (5 * (y ** 2 + 10000) ** 1.5) + (100 - y) * (y - 100) / (3 * ((100 - y) ** 2 + 10000) ** 1.5) + 1 / (3 * m.sqrt((100 - y) ** 2) + 10000)
DDf = lambda y: 10000 * (y ** 2 + 10000) ** 1.5 + 6000 * ((100 - y) ** 2 + 10000) ** 1.5 / (
        3 * ((100 - y) ** 2 + 10000) ** 1.5 * (y ** 2 + 10000) ** 1.5)


def newton(x0, max_iter):
    xn = x0
    for n in range(0, max_iter):
        Dfxn = Df(xn)
        if abs(Dfxn) < TOL:
            print('Lösung nach', n, 'durchläufen gefunden.')
            return xn
        DDfxn = DDf(xn)
        if DDfxn == 0:
            print('Es wurde keine Lösung gefunden.')
            return None
        xn = xn - (Dfxn / DDfxn) * 1000000000000
    print('Anzahl der max. Durchläufe überschritten. Es wurde keine Lösung gefunden')
    return None


def diagonale(x, y, v):
    s = m.sqrt(m.pow(x, 2) + m.pow(y, 2))
    return s / v


def aussagekraeftigerPlot(x, y):
    t = npy.arange(0, 100)
    f = 1 / 3 * npy.sqrt((100 - t) ** 2 + 100 ** 2) + 1 / 5 * npy.sqrt(100 ** 2 + t ** 2)
    # f = ((t - 100) / (3 * npy.sqrt((100 - t) ** 2 + 100 ** 2))) + t / (5 * npy.sqrt(100 ** 2 + t ** 2))
    plt.plot(t, f, label='f(x)')
    plt.scatter(x, y)
    plt.annotate('von Sand ins Wasser\n(Extrempunkt)', xy=(x, y), xytext=(55, 62), arrowprops={'facecolor': 'b'})
    plt.xlabel('x')
    plt.ylabel('Zeit t [s]')
    plt.title('Wann David Haselnuss am schnellsten bei Pam?')
    plt.legend()
    plt.grid(True)
    plt.show()


def aussagekraeftigerPlot2(x, y):
    t = npy.arange(0, 100)
    df = ((t - 100) / (3 * npy.sqrt((100 - t) ** 2 + 100 ** 2))) + t / (5 * npy.sqrt(100 ** 2 + t ** 2))
    plt.plot(t, df, label='Df(x)')
    plt.scatter(x, y)
    plt.annotate('Optimum (Nullstelle)', xy=(x, y), xytext=(75, 0), arrowprops={'facecolor': 'b'})
    plt.xlabel('t')
    plt.ylabel('Df(t)')
    plt.title('Wann David Haselnuss am schnellsten bei Pam?')
    plt.legend()
    plt.grid(True)
    plt.show()


x0 = 50
approx = newton(x0, 10000000)
if approx is not None:
    print(round(approx, 12))  # runden des Ergebnisses auf 6 Nachkommastellen
else:
    print(approx)
b1 = diagonale(100, 100, 5) + diagonale(100, 100, 3)
print("Wie lange braucht David, um Pam zu retten? (Folie 4 - 13)"
      "\nEr braucht", round(b1, 4), "sec.")
b2 = diagonale(100, 200, 5) + diagonale(100, 0, 3)
print("In welchem Fall ist David schneller? (Folie 4 - 14)"
      "\nBild 1: %f, Bild 2: %f -> Bei Variante 1 ist David schneller bei Pam" % (b1, b2))
print("Wie können wir nun diese Nullstelle berechnen?"
      "\nMit dem Newton Verfahren: ", approx)
aussagekraeftigerPlot(approx, f(approx))
aussagekraeftigerPlot2(approx, Df(approx))
