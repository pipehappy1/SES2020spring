import numpy as np
import random as rd
import math
from math import pi
from numpy import cos, sin
from matplotlib import pyplot as plt

m=5
r=0
e=0.01
Px=2*np.random.rand(m)-1
Py=2*np.random.rand(m)-1
U=np.zeros([2,5])
Dijx=0
Dijy=0
dijx=0
dijy=0
while (abs((4 - m*pi*r*r) / 4) > 0.01):
  for i in range(m):
   for j in range(m):
    if i != j:
      dijx=(Px[i] - Px[j]) / abs(Px[i] - Px[j]) * max(2 * r - math.sqrt((Px[i] - Px[j]) ** 2 + (Py[i] - Py[j]) ** 2),0)
      dijy=(Py[i] - Py[j]) / abs(Py[i] - Py[j]) * max(2 * r - math.sqrt((Px[i] - Px[j]) ** 2 + (Py[i] - Py[j]) ** 2),0)
      Dijx=Dijx + dijx
      Dijy=Dijy + dijy
   X_dijboundary=- max(Px[i] + r - 1,0) + max(- (Px[i] - r + 1),0)
   Y_dijboundary=- max(Py[i] + r - 1,0) + max(- (Py[i] - r + 1),0)
   U[0][i]=Dijx + X_dijboundary
   U[1][i]=Dijy + Y_dijboundary
   print(U)
  if U.all() < 0.001:
   r=r + 0.0001
  for h in range(m):
   Px[h]=Px[h] + e*U[0][h]
   Py[h]=Py[h] + e*U[1][h]
  print(r)
  print(abs(4 - m*pi*r*r / 4))
theta=[i*pi/180 for i in range(0,360)]
fig=plt.figure()
for q in range(m):
   x=sin(theta)
   y=cos(theta)
   plt.plot(Px[q]+r*x,Py[q]+r*y,'r')
   
plt.show()