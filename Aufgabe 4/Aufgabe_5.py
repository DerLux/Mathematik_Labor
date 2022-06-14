import math as m

TOL = 1e-12
alpha = 2
De = lambda y: ((p[0][1] - alpha * m.e ** (y * p[0][0])) * p[0][0] * m.e ** (y * p[0][0]) + (
                 p[1][1] - alpha * m.e ** (y * p[1][0])) * p[1][0] * m.e ** (y * p[1][0]) + (
                 p[2][1] - alpha * m.e ** (y * p[2][0])) * p[2][0] * m.e ** (y * p[2][0]) + (
                 p[3][1] - alpha * m.e ** (y * p[3][0])) * p[3][0] * m.e ** (y * p[3][0]))

DDe = lambda y: ((p[0][0] * p[0][0] * m.e ** (y * p[0][0]) * (p[0][1] - 2 * alpha * m.e ** (y * p[0][0]))) + (
                  p[1][0] * p[1][0] * m.e ** (y * p[1][0]) * (p[1][1] - 2 * alpha * m.e ** (y * p[1][0]))) + (
                  p[2][0] * p[2][0] * m.e ** (y * p[2][0]) * (p[2][1] - 2 * alpha * m.e ** (y * p[2][0]))) + (
                  p[3][0] * p[3][0] * m.e ** (y * p[3][0]) * (p[3][1] - 2 * alpha * m.e ** (y * p[3][0]))))

p1 = (0.2, 2.4)
p2 = (0.4, 3.6)
p3 = (0.6, 2.9)
p4 = (0.8, 4.3)

p = [p1, p2, p3, p4]


def newton(x0, max_iter):
    xn = x0
    for n in range(0, max_iter):
        Dfxn = De(xn)
        if abs(Dfxn) < TOL:
            print('Lösung nach', n, 'durchläufen gefunden.')
            return xn
        DDfxn = DDe(xn)
        if DDfxn == 0:
            print('Es wurde keine Lösung gefunden.')
            return None
        xn = xn - (Dfxn / DDfxn)
    print('Anzahl der max. Durchläufe überschritten. Es wurde keine Lösung gefunden')
    return None


x0 = 2
ergebnis = newton(x0, 100000)

print(round(ergebnis, 12))
