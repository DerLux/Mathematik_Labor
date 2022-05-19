import math
import numpy as np

from collections import OrderedDict
from matplotlib import pyplot as plt

print("Authors: Tobias Stöhr, Lukas Butscher, Wiebke Prinz, Jona Böcker")

t = [0] * 4201
b = [0] * 4201
k = [0] * 51
K = [0] * 4201
ball = [0] * 4201
Ball = [0] * 4201
alpha = 2 * 10 ** -2
gamma = 2100
beta = 2 * gamma ** -2

for x in range(0, 4201):
    t[x] = x
    b[x] = alpha * math.exp((-beta * (x - gamma) ** 2))
    if x == 0:
        ball[x] = 0
        Ball[x] = 0
    else:
        ball[x] = ball[x - 1] + b[x]
        Ball[x] = math.floor(ball[x - 1] + b[x])

for x in range(0, 4201):
    ball[x] = round(ball[x])
B = list(OrderedDict.fromkeys(ball))

# print("\n", b)
# print("\n", t)
# print("\n", ball)
# print("\n", Ball)
# print("\n", B)

a = plt.figure(2)
plt.scatter(t, ball)
plt.title("Anwesende Personen B(T)")
plt.xlim([0, t[len(t) - 1]])
plt.ylim([0, ball[len(t) - 1]])
plt.xlabel("Zeit T")
plt.ylabel("Personen B")
plt.grid(alpha=0.5)
a.show()

print("\nAm Ende sind", ball[len(ball) - 1], "Besucher im Kino\n")

b = plt.figure(2)
plt.scatter(ball, t)
plt.title("Ankunftszeiten T(B)")
plt.xlim([0, ball[len(t) - 1]])
plt.ylim([0, t[len(t) - 1]])
plt.xlabel("Personen B")
plt.ylabel("Zeit T(B)")
plt.grid(alpha=0.5)
b.show()

for x in B:
    if x != 0:
        k[x] = math.floor(math.log(B[x]) + 0.5)

c = plt.figure(2)
plt.scatter(B, k)
plt.title("Kassen je Personen K(B)")
plt.xlim([0, B[len(B) - 1]])
plt.ylim([0, k[len(k) - 1]])
plt.xlabel("Personen B")
plt.ylabel("Kassen K(B)")
plt.grid(alpha=0.5)
c.show()

print("\na)")
for x in range(2, len(Ball)):
    if Ball[x - 1] != 0:
        w = math.floor(math.log(Ball[x]) + 0.5)
        q = math.floor(math.log(Ball[x - 1]) + 0.5)
        if w != q:
            K[x] = 1
            print('   Kassenöffnung nach %.2f Minuten' % (t[x] / 60))
        else:
            K[x] = 0

d = plt.figure(2)
plt.scatter(t, K)
plt.title("Kassenöffnung nach Zeit")
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.ylim([0, 1])
plt.xlim([0, t[len(t) - 1]])
plt.ylabel("Kassenöffnungen")
plt.xlabel("Zeit T(B)")
plt.grid(alpha=0.5)
d.show()


print("\nb) Es kommen insgesamt", B[len(B) - 1], "Personen ins Kino\n")
print("c) Wir hätten uns keine schönere beschäftigung für einen Montag Nachmittag vorstellen können\n")
