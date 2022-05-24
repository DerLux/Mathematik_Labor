import math as m

print("Authors: Tobias Stöhr, Lukas Butscher, Wiebke Prinz, Jona Böcker\n")

TOL = 1e-12  # Abbruchbedingung
f = lambda y: 1 / 3 * m.sqrt((100 - y) ** 2 + 100 ** 2) + 1 / 5 * m.sqrt(100 ** 2 + y ** 2)  # Funktion
Df = lambda y: ((y - 100) / (3 * m.sqrt((100 - y) ** 2 + 100 ** 2))) + (y / (5 * m.sqrt(100 ** 2 + y ** 2)))  # Abl


#f = lambda x: x ** 3 - x ** 2 - 1  # Funktion
#Df = lambda x: 3 * x ** 2 - 2 * x  # Ableitung


def newton(x0, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < TOL:
            print('Lösung nach', n, 'durchläufen gefunden.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Es wurde keine Lösung gefunden.')
            return None
        xn = xn - fxn / Dfxn
    print('Anzahl der max. Durchläufe überschritten. Es wurde keine Lösung gefunden')
    return None


# print("", Df(108))

approx = newton(100, 1000)
if approx is not None:
    print(round(approx, 6))  # runden des Ergebnisses auf 6 Nachkommastellen
else:
    print(approx)
