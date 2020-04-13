import unittest
from elevator2 import Building
from elevator2 import Elevator
from elevator2 import Customer

# assertEqual(a,b)  a==b              assertNotEqual(a,b) a!=b
# assertIn(item,list) item in list    assertNotIn(item,list)  item not in list
# assertTrue(x)  x为True              assertFalse(x) x为False

class TestElevator(unittest.TestCase):
    #测试 elevator中的类Elevator
    def setUp(self):
        # 做些初始化操作
        # 创建类并设置属性
        # Python 将先运行它，各个方法中创建的对象，在此方法中创建，并且就创建一次，其他方法中都不用创建。
        self.my_Elevator = Elevator(6)
        self.tempfloor=self.my_Elevator.cur_floor
        self.tempdirection=self.my_Elevator.direction
 
    def test_move(self):
        self.my_Elevator.move()
        self.assertEqual(self.my_Elevator.cur_floor,self.tempfloor+self.tempdirection)

    def test_register_customer(self):
        self.my_Elevator.register_customer(1)
        self.assertIn(1,self.my_Elevator.register_list)

    def test_cancel_customer(self):
        self.my_Elevator.register_customer(1)
        self.my_Elevator.cancel_customer(1)
        self.assertNotIn(1,self.my_Elevator.register_list)
 

if __name__ == '__main__':
    unittest.main()