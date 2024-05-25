from control import *

# Define system transfer function
G = tf(1, [1, 4])

# Define lead compensator parameters
a = 4
b = 5.2

# Create lead compensator transfer function
C = tf(K * (s + a), s + b)

# Combine system and compensator
G_c = G * C

# Perform root locus analysis
rlocus(G_c)

# Adjust K value by hand in the plot to observe pole movement
