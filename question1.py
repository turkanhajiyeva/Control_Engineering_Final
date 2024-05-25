import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 25, 0.01)

G = cn.tf([1], [1,4,0])

print(G)

cn.rlocus(G)
plt.title('Root Locus of Closed Loop System')

K_values = [5, 25, 50, 70, 110]

for K in K_values:
    clsys = K * G / (1 + K * G)
    plt.figure()
    cn.pzmap(clsys)
    plt.title(f'Pole-Zero Map for K={K}')

    y, T = cn.step(clsys, t)
    def find_ts(t, y):
        i = y.size - 1
        while (True):
            if (y[i] - 1) ** 2 > (0.02) ** 2:
                return t[i]
                break
            else:
                i = i - 1

    ts = find_ts(t, y)
    def find_tr(t, y):
        i = 0  # soldan basliyiriq
        while (True):
            if (y[i]) > 1.00:
                tr = t[i]
                return tr
                break
            else:
                i = i + 1

    tr = find_tr(t, y)

    y_max_index = np.argmax(y)
    mp = y[y_max_index] - 1
    print(ts)
    print(tr)
    print(mp)

    plt.figure()
    plt.plot(t, y, label=f'Settling time for K={K}: {ts:.2f} seconds')
    plt.plot(t, y, label=f'Rising time for K={K}: {tr:.2f} seconds')
    plt.plot(t, y, label=f'Maximum Overshoot for K={K}: {mp:.2f}')
    plt.legend()

plt.show()