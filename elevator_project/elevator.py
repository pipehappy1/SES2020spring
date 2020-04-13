# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:09:40 2020

@author: 85726
"""

"""
模拟电梯运行：
该代码模拟了某一楼层的电梯状态，为简化模型，假设要乘坐电梯的所有人在不同楼层同时按下了电梯键，电梯要做出最节省时间的方案将所有人运送到目标楼层
电梯初始在随机的楼层，此时会根据电梯所在的楼层，如果在上半层，电梯默认初始往下运行，反之亦然
如果电梯运行方向的楼层无乘客以及电梯内的乘客已经到达目标楼层时，电梯运行方向才会改变
如果电梯运行途中的楼层有去向相同的乘客，则乘客进入电梯，如果电梯运行方向与乘客要去的方向相反，则乘客会在原楼层等待
当电梯完成所有乘客的运输后，会停在最后一名乘客的目的楼层
"""

import random
import time

class Building():
    def __init__(self, floors, customers):
        self.floors = floors # 楼层数量
        # 创造一列乘客信息
        self.customer_list = []
        self.unfinished_customer_list = []
        for i in range(customers):
            cur_floor = random.randint(1,floors)
            choice_list = list(range(1, floors+1))
            choice_list.remove(cur_floor) #不会出现乘客乘坐电梯不移动楼层的情况，故去除当前层取值
            dst_floor = random.choice(choice_list)
            UorD = int(abs(dst_floor-cur_floor) / (dst_floor-cur_floor))
            self.customer_list.append(Customer(cur_floor, dst_floor, i+1, UorD))   #电梯乘客包含当前楼层，目标楼层，乘客id，方向参数
        self.unfinished_customer_list = list(self.customer_list) #初始化所有要乘坐电梯的乘客
        
        self.elevator = Elevator(floors) # 为楼层配置一个电梯，输入楼层数
        

    def run(self):
        """operate the elevator"""
        #先判断中途转向，再判断乘客进出
        
        #电梯中途不改变方向的条件：运行方向上的任一楼层没有未进电梯的乘客 or 电梯内任一乘客没到达
        direction_change = []   #乘客进行投票，0为不同意，一旦有0就不改向
        
        #取出运行方向上剩余的楼层号(不包括当前楼层)
        if self.elevator.get_direction() > 0:
            floors_list = list(range(self.elevator.get_cur_floor()+1, self.floors+1)) 
        else:
            floors_list = list(range(1, self.elevator.get_cur_floor())) 
        
        #遍历未finished的乘客
        for customer in self.unfinished_customer_list:
            #对于在电梯里的乘客判断是否改向，默认电梯内customer.get_UorD() == self.elevator.get_direction()
            if customer.get_ID() in self.elevator.get_register_list():
                #if customer.get_UorD() == self.elevator.get_direction():
                if customer.get_dst_floor() != self.elevator.get_cur_floor():
                    direction_change.append(0) #同方向且乘客未到达，不同意改向
            
            # 对于不在电梯里的乘客判断是否改向
            else:
                #判断floors_list内是否有未进电梯的乘客
                if customer.get_cur_floor() in floors_list:
                    direction_change.append(0) 
                #判断当前层是否有未进电梯的乘客
                if customer.get_cur_floor() == self.elevator.get_cur_floor() :
                    if customer.get_UorD() == self.elevator.get_direction():
                        direction_change.append(0) #若该乘客去的方向和电梯方向一致(即将入电梯)，不同意改向
                    
        #中途改变运行方向
        if not 0 in direction_change:
            self.elevator.direction *= -1
            print('change direction')
            
        # 检查每位乘客
        for customer in self.customer_list:
            # 如果乘客在电梯内
            if customer.get_ID() in self.elevator.get_register_list():
                # 如果乘客到达了目标楼层
                if customer.get_dst_floor() == self.elevator.get_cur_floor():
                    customer.move_out()
                    self.elevator.cancel_customer(customer.get_ID())
                    self.unfinished_customer_list.remove(customer)
            # 如果乘客不在电梯内
            else:
                #增加第三个判断条件：如果电梯运行方向与乘客希望去的方向不一致，那么乘客暂时不进电梯；方向一致，进电梯  
                if (not customer.has_finished()) and \
                (customer.get_cur_floor() == self.elevator.get_cur_floor()) and \
                (customer.get_UorD() == self.elevator.get_direction()):
                    customer.move_in()
                    self.elevator.register_customer(customer.get_ID())

        # 电梯移动
        if not self.has_finished():
            self.elevator.move()
            # 特殊情况限定电梯不会到达高于楼层的地方和地下
            if (self.elevator.get_cur_floor()+self.elevator.get_direction() < 1) or \
            (self.elevator.get_cur_floor()+self.elevator.get_direction() > self.floors):
                self.elevator.direction *= -1
            
    
    def output(self):
        """output the building"""
        LEFT = 10
        CENTER = 60
        RIGHT = 10
        print ('-'*(LEFT+CENTER+RIGHT))
        print ("Floor".center(LEFT)+"Customer".center(CENTER)+"Elevator".center(RIGHT))
        print ('-'*(LEFT+CENTER+RIGHT))

        for i in range(self.floors, 0, -1):
            line = str(i).center(LEFT)
            customer_print_list = []
            #customer打印格式： ID,up or down,finished or not
            for customer in self.customer_list:
                if (not customer.is_in_elevator()) and customer.get_cur_floor() == i:
                    customer_print_list.append(str(customer.get_ID())+','+str(customer.get_UorD())+','+str(customer.has_finished()))
            line += ';  '.join(customer_print_list).center(CENTER)
            if i == self.elevator.get_cur_floor():
                line += 'X'.center(RIGHT)
            print(line)  #打印当前行的信息：floor + customer + elevator
            print('-'*(LEFT+CENTER+RIGHT))

    def get_customer_list(self):#得到全部乘客的信息
        """return the customer_list"""
        return self.customer_list

    def has_finished(self):#判断电梯是否已经将所有人送到目的楼层，完成返回True
        """check whether all customers have reached dst_floors"""
        for customer in self.get_customer_list():
            if not customer.has_finished():
                return False
        return True

class Elevator():
    def __init__(self, floors):
        self.floors = floors # 楼层数
        self.register_list = [] # 电梯内的乘客表
        self.cur_floor = random.randint(1,floors) # 模拟电梯初始楼层随机
        #若电梯的位置处于building的上半层，则往下；在下半层，则往上
        self.direction = -1 if self.cur_floor/self.floors >= 1/2 else 1  # 1:上; -1:下

    def move(self):
        """move the elevator by 1 floor"""
        #移动电梯
        self.cur_floor += self.direction

    def register_customer(self, customer):#移动某位乘客进入电梯序列中
        """put the customer into register_list (ID)"""
        self.register_list.append(customer)

    def cancel_customer(self, customer):#删除电梯序列中的某位乘客
        """remove the customer from register_list (ID)"""
        self.register_list.remove(customer)

    def in_register_list(self, customer):#检查某位乘客是否在电梯内
        """check whether the customer is in register_list: in -> 1 ; out -> 0"""
        return customer in self.register_list

    def get_register_list(self):#得到目前在电梯内的乘客表
        """return register_list"""
        return self.register_list

    def get_cur_floor(self):#电梯目前所在楼层
        """return current floor"""
        return self.cur_floor
    
    def get_direction(self):#电梯完成运输后最后所在的楼层
        """return current floor"""
        return self.direction

class Customer():#乘客信息
    def __init__(self, cur_floor, dst_floor, ID, UorD):
        self.cur_floor = cur_floor
        self.dst_floor = dst_floor
        self.ID = ID
        self.in_elevator = False # 初始乘客不在电梯内
        self.finished = False # 初始乘客未到达目标楼层
        self.UorD = UorD # 1表示乘客向上，-1表示向下

    def get_cur_floor(self):#获得乘客当前所在楼层
        """return current floor"""
        return self.cur_floor

    def get_dst_floor(self):#获得乘客目标楼层
        """return destination floor"""
        return self.dst_floor

    def get_ID(self):
        """return customer's ID"""
        return self.ID
    
    def get_UorD(self):
        """return customer's ID"""
        return self.UorD

    def move_in(self):#当前乘客进入了电梯
        """move the customer into the elevator"""
        self.in_elevator = True

    def move_out(self):#乘客离开电梯
        """move the customer out of the elevator"""
        self.in_elevator = False
        self.finished = True
        self.cur_floor = self.dst_floor

    def has_finished(self):#返回乘客是否到达了目标楼层，到达返回True
        """check whether the customer has reached the dst_floor"""
        return self.finished

    def is_in_elevator(self):#返回乘客是否在电梯内，在返回True
        """check whether the customer is in the elevator"""
        return self.in_elevator

def main():
    floors = input("Please input how many floors in this building: ")
    while not floors.isdigit():
        floors = input("Please input how many floors in this building: ")
    customers = input("Please input how many customers in this building: ")
    while not customers.isdigit():
        customers = input("Please input how many customers in this building: ")
    building = Building(int(floors), int(customers))
    building.output()

    # 电梯移动直到最后的一位乘客到达目标楼层
    count = 0
    while not building.has_finished():
        time.sleep(1)
        building.run()
        building.output()
        count += 1
    print('the total floors that the elevator moves: '+str(count))
    
if __name__ == '__main__':
    main()
    
