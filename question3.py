import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 25, 0.01)

G = cn.tf([1], [1,0,0])
print(G)

cn.rlocus(G)
plt.title('Root Locus')

K_values = [5, 10, 15]

for K in K_values:
    clsys = K * G / (1 + K * G)
    plt.figure()
    cn.pzmap(clsys)
    plt.title(f'Pole-Zero Map for K={K}')
    y, T = cn.step(clsys, t)
    plt.figure()
    plt.plot(t, y, label=f'K={K}')
    plt.legend()

plt.show()