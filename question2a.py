import numpy as np
import matplotlib.pyplot as plt
import control.matlab as cn

t = np.arange(0, 25, 0.01)

# Case 1: L = 0
num1 = [1]
den1 = [1, 4, 1]
G1 = cn.tf(num1, den1)

print(G1)

# Case 2: L != 0
num2 = [1]
den2 = [(0.1/4), 1, 4.025, 1]
G2 = cn.tf(num2, den2)

print(G2)

# Proportional gain
K = -1

# Closed-loop systems
CL_sys1 = cn.feedback(K * G1)
CL_sys2 = cn.feedback(K * G2)

# Pole-zero plot for both systems
cn.pzmap(CL_sys1)
plt.figure()
cn.rlocus(CL_sys1)
plt.figure()
cn.pzmap(CL_sys2)
plt.figure()
cn.rlocus(CL_sys2)

# Step response for both systems
t1, response1 = cn.step(CL_sys1, t)
t2, response2 = cn.step(CL_sys2, t)

# Plotting the step responses
plt.figure()
plt.plot(response1, t1, label='L = 0')
plt.plot(response2, t2, label='L ≠ 0')
plt.title('Step Response for Both Systems')
plt.legend()
plt.show()