import numpy as np
import random as rd
import math
from numpy import cos, sin
from matplotlib import pyplot as plt
m=5
r=0
e=0.001
Px=np.dot(2,np.random.randn(10)) - 1
Py=np.dot(2,np.random.randn(10)) - 1
U=np.ones((2,m))*0
Dijx=0
Dijy=0
while abs((4 - np.dot(np.dot(np.dot(m,math.pi),r),r)) / 4) > 0.1:
 for i in range(m):
  for j in range(m):
   if i != j:
     dijx=np.dot((Px(i) - Px(j)) / abs(Px(i) - Px(j)),max(np.dot(2,r) - sqrt((Px(i) - Px(j)) ** 2 + (Py(i) - Py(j)) ** 2),0))
     dijy=np.dot((Py(i) - Py(j)) / abs(Py(i) - Py(j)),max(np.dot(2,r) - sqrt((Px(i) - Px(j)) ** 2 + (Py(i) - Py(j)) ** 2),0))
     Dijx=Dijx + dijx
     Dijy=Dijy + dijy
     X_dijboundary=- max(Px(i) + r - 1,0) + max(- (Px(i) - r + 1),0)
     Y_dijboundary=- max(Py(i) + r - 1,0) + max(- (Py(i) - r + 1),0)
     U[0,i]=Dijx + X_dijboundary
     U[1,i]=Dijy + Y_dijboundary
     if U < 0.0001:
        r=r + 1e-05
   for h in range(m):
       Px[h]=Px[h] + np.dot(e,U(0,h))
       Py[h]=Py[h] + np.dot(e,U(1,h))
theta=[i*math.pi/180 for i in range(0,360)]
for q in range(m):
    plot(Px(q) + np.dot(r,sin(theta)),Py(q) + np.dot(r,cos(theta)),'r')
    hold('on')
plt.axis('equal')
plt.axis('scaled')
plt.show()