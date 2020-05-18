import unittest
import matplotlib.pyplot as plt
import numpy as np
from circle_packing import circle
from circle_packing import check, search

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = circle(0.5,0.5,0.5)
        self.c2 = circle(-0.5,-0.5,0.5)
        self.c3 = circle(0.5,0,0.5)
        self.c4 = circle(-0.5,0.5,0.5)

    def test_check(self): ##检查check()
        clist=[]
        clist.append(self.c1)
        clist.append(self.c2)
        self.assertTrue(check(self.c4, clist)) ##判断c4是否和list里的圆有重叠，预期是返回1，无重叠
        self.assertFalse(check(self.c3, clist)) ##判断c3是否和list里的圆有重叠，预期是返回0，有重叠

    def test_search(self):
        clist = []
        clist.append(self.c1)
        clist.append(self.c2)
        search(clist)     ##假设现在已经有c1，c2了，在此基础上寻找能塞入盒子中的最大圆
        self.assertEqual(clist[2].x ,self.c4.x)##search得到的新的最大圆应为c4（在第二象限）
        self.assertEqual(clist[2].y, self.c4.y)##似乎不允许把圆与圆整体作比较,因此这里分别比对它们的参数
        self.assertEqual(clist[2].r, self.c4.r)

if __name__ == '__main__':
    unittest.main(verbosity=2)
