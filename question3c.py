import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 25, 0.01)

G = cn.tf([1], [1,0, 0])

print(G)

lead_comp = cn.tf([1,0], [1, 2])

Gnew = G * lead_comp
K = 2.84

clsys = K * Gnew / (1 + K * Gnew)
plt.figure()
cn.pzmap(clsys)
plt.title(f'Pole-Zero Map for K={K}')

y, T = cn.step(clsys, t)
y_ramp, T, x = cn.lsim(clsys, t, t)


def find_ts(t, y):
    for i in range(y.size - 1, -1, -1):
        if (y[i] - 1) ** 2 > (0.02) ** 2:
            return t[i]
    return t[-1]

ts = find_ts(t, y)

def find_tr(t, y):
    for i in range(y.size):
        if y[i] > 1.00:
            return t[i]
    return t[-1]

tr = find_tr(t, y)

y_max_index = np.argmax(y)
mp = y[y_max_index] - 1
print(f"K={K}: Settling time={ts}, Rising time={tr}, Maximum Overshoot={mp}")

plt.figure()
plt.plot(t, y, label=f'Settling time for K={K}: {ts:.2f} seconds')
plt.plot(t, y, label=f'Rising time for K={K}: {tr:.2f} seconds')
plt.plot(t, y, label=f'Maximum Overshoot for K={K}: {mp:.2f}')
plt.legend()

plt.figure()
plt.plot(t, t)
plt.plot(t, y_ramp)
plt.show()