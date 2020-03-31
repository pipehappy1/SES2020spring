import unittest
import numpy as np
from circle_pack import circle
from circle_pack import *

class test_case1(unittest.TestCase)
    def test_initialize(self):
        self.c1 = circle(0,0,0)
        self.c2 = circle(1,1,1)
        self.c3 = circle(0.5,0.5,0.5)
        self.c_list = []
        self.c_list.append(self.c2)
        self.c_list.append(self.c3)

    def test_distance(self):
        distance_cal=self.c1.distance(self.c2)
        distance=np.linalg.norm([self.c1.x-self.c2.x,self.c1.y-self.c2.y])
        self.assertEqual(distance, distance_cal)

if __name__ == '__main__':

    unittest.main(verbosity=2)