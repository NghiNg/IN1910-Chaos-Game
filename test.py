import numpy as np
a = []
theta = 2*np.pi/4
theatre = [theta]
for i in range(3):
    theatre.append(theatre[i]+theta)
for i in range(4):
    a.append([np.sin(theatre[i]), np.cos(theatre[i])])
a = np.array(a)
print(a)
