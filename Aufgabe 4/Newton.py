import math as m

print("Authors: Tobias Stöhr, Lukas Butscher, Wiebke Prinz, Jona Böcker\n")

TOL = 1e-12  # Abbruchbedingung
f = lambda y: 1 / 3 * m.sqrt((100 - y) ** 2 + 100 ** 2) + 1 / 5 * m.sqrt(100 ** 2 + y ** 2)  # Funktion
Df = lambda y: ((y - 100) / (3 * m.sqrt((100 - y) ** 2 + 100 ** 2))) + y / (5 * m.sqrt(100 ** 2 + y ** 2))  # Abl
# DDf = lambda y: 1 / (5 * m.sqrt(y ** 2 + 10000)) - y ** 2 / (5 * (y ** 2 + 10000) ** 1.5) + (100 - y) * (y - 100) / (3 * ((100 - y) ** 2 + 10000) ** 1.5) + 1 / (3 * m.sqrt((100 - y) ** 2) + 10000)
DDf = lambda y: 10000 * (y ** 2 + 10000) ** 1.5 + 6000 * ((100 - y) ** 2 + 10000) ** 1.5 / (3*((100 - y) ** 2 + 10000) ** 1.5 * (y ** 2 + 10000) ** 1.5)


def newton(x0, max_iter):
    xn = x0
    for n in range(0, max_iter):
        Dfxn = Df(xn)
        if abs(Dfxn) < TOL:
            print('Lösung nach', n, 'durchläufen gefunden.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Es wurde keine Lösung gefunden.')
            return None
        xn = xn - fxn / Dfxn
    print('Anzahl der max. Durchläufe überschritten. Es wurde keine Lösung gefunden')
    return None


x0 = 1
approx = newton(x0, 10000000)
if approx is not None:
    print(round(approx, 12))  # runden des Ergebnisses auf 6 Nachkommastellen
else:
    print(approx)
