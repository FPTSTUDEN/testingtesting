try:
    from testingtesting.assignments.as9.e123 import Car
except ImportError:
    import sys, os
    # add parent of the "testingtesting" package to sys.path so the absolute import works
    package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    print(sys.path)
    if package_root not in sys.path:
        sys.path.insert(0, package_root)
    from testingtesting.assignments.as9.e123 import Car as 车
import random
class 电动车(车):
    def __init__(self, 型号, 最大速度, 电池容量):
        super().__init__(型号, 最大速度)
        self.电池容量 = 电池容量
    #     self.当前电量 = 电池容量
    # def 充电(self, 电量增加):
    #     self.当前电量 += 电量增加
    #     if self.当前电量 > self.电池容量:
    #         self.当前电量 = self.电池容量
class 汽油车(车):
    def __init__(self, 型号, 最大速度, 油箱容量):
        super().__init__(型号, 最大速度)
        self.油箱容量 = 油箱容量
    #     self.当前油量 = 油箱容量
    # def 加油(self, 油量增加):
    #     self.当前油量 += 油量增加
    #     if self.当前油量 > self.油箱容量:
    #         self.当前油量 = self.油箱容量
if __name__ == "__main__":
    # 电车 = 电动车("特斯拉 Model S", 250, 100)
    # 油车 = 汽油车("丰田 卡罗拉", 180, 50)
    电车 = 电动车("ABC-15", 180, 52.5)
    油车 = 汽油车("ACD-123", 165, 32.3)
    for 车 in (电车, 油车):
        车.accelerate(random.randint(20, 车.max_speed))
        车.drive(3)
    for 车 in (电车, 油车):
        print("-----")
        print(f"型号: {车.registration_number}")
        print(f"行驶距离: {车.traveled_distance} km")
    print("-----")
    # print(f"电动车属性:")
    # for 属性, 值 in vars(电车).items():
    #     print(f"{属性}: {值}")
    # print("-----")
    # print(f"汽油车属性:")
    # for 属性, 值 in vars(油车).items():
    #     print(f"{属性}: {值}")