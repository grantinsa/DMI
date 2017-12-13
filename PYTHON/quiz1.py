import random
import numpy as np

def ranges(bars_ranges_local,bars_local,x_local):
    for i in range(len(x_local)):
        for j in range(len(bars_ranges_local)-1):
            if x_local[i] > bars_ranges_local [j]: 
            and x_local[i] < bars_ranges_local [j+1]
                bars_local[j] = bars_local[j] + 1
                if x_local[1] > bars_ranges_local[j+1]:
                    bars_local[j+1] = bars_local[j+1] + 1
            return b

N = 5 
x = []
a = 0
b = np.pi
delta = 0.5
for i in range(N):
    x.append(random.uniform(a,b))
    #x.append(random.triangular(a,b))

bars_ranges = np.arange(a,b,delta)
bars = np.zeros(len(bars_ranges))
print bars
bars = ranges(bars_ranges,bars,x)
print bars
