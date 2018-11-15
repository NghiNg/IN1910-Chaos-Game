import numpy as np
color = [0,1,0,0,2]
test = [1,2,3,4,5]
for i in range(len(color)):
    print(color[i]==0)
    red = test[color[i] == 0]
    print(red)
