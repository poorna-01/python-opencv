import sklearn
import matplotlib.pyplot as plt
import numpy as np
#import random

#y=mx+c
#F=1.8*C+32

x = list(range(0,10))
y = [1.8*F+32 for F in x]

#y = [1.8*F+32 + random.randint(-3,3) for F in x]

print(f'x:{x}')
print(f'y:{y}')

plt.plot(x,y,'-*r')
plt.show()

