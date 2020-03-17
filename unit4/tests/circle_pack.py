# coding: utf-8

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import minimize

#定义一个类
class circle:
    def __init__(self, radius = 0, x = 0, y = 0):
        self.radius = radius
        self.x = x
        self.y = y
    
#打印圆的半径和圆心坐标    
    def print_circle(self):
        print('r={}, (x,y)=({},{})'.format(self.radius, self.x, self.y))
    
#计算两圆心之间的距离
    def distance(c1, c2):       
        D = ((c1.x-c2.x)**2+(c1.y-c2.y)**2)**0.5
        return D
    
#判断另一个与现存圆是否相交，相交为0，全不相交为1 
    def overlap_or_not(self, c_list):
        for c in c_list:
            r1 = self.radius
            r2 = c.radius
            rr = r1+r2
            dis = self.distance(c)
            if dis < rr:
                return 0
        return 1
        
#判断圆是否越界，越界为0，不越界为1 
    def excess_or_not(self):
        x = self.x
        y = self.y
        r = self.radius
        left = abs(x - r)
        right = abs(x + r)
        upper = abs(y + r)
        lower = abs(y - r)
        if max(left, right, upper, lower) > 1:
            return 0
        return 1

#找出最大可行半径
def FindR(c1, c_list):
    x = c1.x
    y = c1.y
    R_list = [1-x,1+x,1-y,1+y]
# 计算到其他各圆的距离
    for c in c_list:
            r = c.distance(c1) - c.radius
            R_list.append(r)
# 从中取最小值，即最大可行半径
    return min(R_list)

#需要优化的目标函数        
def func(c_list):
    return lambda x : 1 - FindR(circle(x[0], x[1], x[2]), c_list)

#找出最优圆心
def Find_Center(c, c_list):
    r = c.radius
    x = c.x
    y = c.y
    rxy = [r,x,y]
    limit_r = (0, 1)
    limit_x = (-1, 1)
    limit_y = (-1, 1)
    bds = (limit_r, limit_x, limit_y)       
    res = minimize(func(c_list), rxy, method='SLSQP', bounds=bds)
    c.x = res.x[1]
    c.y = res.x[2]
    c.radius = FindR(c, c_list)
    return c

#已知所求圆的个数m，找到剩余空间的最大圆
def FindCircle(m):
    c_list = []
#逐步添加新的圆
    for i in range (m):
        r = 0
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        c = circle(r, x, y)
#满足最大圆的情况
        while not c.overlap_or_not(c_list):           
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            c = circle(r, x, y)
        c = Find_Center(c, c_list)
        c_list.append(c)
    return c_list

def plot(c_list):
    plt.figure()
    plt.axes().set_aspect('equal')
    plt.xlim([-1,1])
    plt.ylim([-1,1])  
    theta = np.linspace(0,2*np.pi,50)
    for c in c_list: 
        plt.plot(c.x+c.radius*np.cos(theta),c.y+c.radius*np.sin(theta),'b') 
    plt.show()
    
if __name__ == "__main__":
    m = 5
    c_list = FindCircle(m)   
    R_squ = 0
    for c in c_list:
        R_squ = R_squ + c.radius**2
        c.print_circle()
    print('for {} circles, the maximize sum of r^2 = {}'.format(m, R_squ))
    plot(c_list)
