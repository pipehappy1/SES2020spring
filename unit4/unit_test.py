# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:38:27 2020

@author: 85726
"""

import unittest
import numpy as np
from FindMCircle import circle
from FindMCircle import *

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = circle(1,0,0)
        self.c2 = circle(0.5,0.5,0.5)
        self.c3 = circle(1,1,1)
        self.c4 = circle(0,-0.5,-0.5)
        self.c_list = []
        self.c_list.append(self.c2)
        self.c_list.append(self.c3)
    
    def test_dis(self):
        dis_c = self.c1.distance(self.c2)
        dis = np.linalg.norm([self.c1.x-self.c2.x,self.c1.y-self.c2.y])
        self.assertEqual(dis_c,dis)
    
    def test_cross(self):
        self.assertEqual(self.c1.ifcross(self.c_list),0)
        
    def test_excess(self):
        self.assertEqual(self.c1.ifexcess(),1)
        self.assertFalse(self.c3.ifexcess(),1)
        
    def test_MaxR(self):
        MR = MaxR(self.c4,self.c_list)
        print(MR)
        self.assertLessEqual(MR,2)
        
    def test_FindMaxCircle(self):
        m = 10
        c_list = FindMaxCircuit(m)
        RR = 0
        for c in c_list:
            RR += c.radius**2
        self.assertGreaterEqual(RR,1)
        
if __name__ == '__main__':
    unittest.main()