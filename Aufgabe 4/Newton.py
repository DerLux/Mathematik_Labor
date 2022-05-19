from sympy import *
import numpy as np

print("Authors: Tobias Stöhr, Lukas Butscher, Wiebke Prinz, Jona Böcker")

def newton(f, Df, x0, epsilon, max_iter):
    """Annähende Lösung von f(x)=0 durch die Newton Methode.

    Parameter
    ----------
    f : Funktion
        Funktion, für welche das Verfahren angewendet werden soll
    Df : Funktion
        Ableitung der Funktion f(x).
    x0 : Zahl
        Anfangswert.
    epsilon : Zahl
        Stoppt, wenn abs(f(x)) < epsilon.
    max_iter : Integer
        Max. Anzahl der Durchläufe.

    Return
    -------
    xn : Zahl
        Annähernde Lösung oder None, wenn es keine Lösung gibt,
        oder die max. Durchläufe überschritten werden
    """
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Lösung nach', n, 'durchläufen gefunden.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Es wurde keine Lösung gefunden.')
            return None
        xn = xn - fxn / Dfxn
    print('Anzahl der max. Durchläufe überschritten. Es wurde keine Lösung gefunden')
    return None

# x = Symbol('x')


p = lambda x: x ** 3 - x ** 2 - 1  # Funktion
Dp = lambda x: 3 * x ** 2 - 2 * x  # Ableitung
# Dp = lambda x: p.diff(x) # Ableitung automatisch berechnen
approx = newton(p, Dp, 1, 1e-10, 10)
print(round(approx, 6))  # runden des Ergebnisses auf 6 nachkommastellen
