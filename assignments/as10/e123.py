#12345678901234567890123456789012345678901234567890123456789012345678901234567890
# 1
class Elevator():
    def __init__(self, bottom: int, top: int):
        self.bottom = -bottom
        self.top = top
        self.current = -bottom
    def floor_up(self):
        self.current += (1 if self.current < self.top else 0)
    def floor_down(self):
        self.current -= (1 if self.current > self.bottom else 0)
    def go_to_floor(self, floor: int):
        while self.current < floor and self.current < self.top:
            self.floor_up()
            print(f"Current floor: {self.current}")
        while self.current > floor and self.current > self.bottom:
            self.floor_down()
            print(f"Current floor: {self.current}")
        print(f"Arrived at floor: {self.current}")
# 2
class Building():
    def __init__(self, bottom: int, top: int, elevators: int):
        self.elevators = [Elevator(bottom, top) for _ in range(elevators)]
        self.bottom = bottom
        self.top = top
    def run_elevator(self, elevator_number: int, floor: int):
        self.elevators[elevator_number].go_to_floor(floor)
    # 3
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
if __name__ == "__main__":
    # 1
    elevator1= Elevator(10,10)
    elevator1.go_to_floor(5)
    elevator1.go_to_floor(elevator1.bottom)
    # 2 
    building = Building(5, 5, 3)
    building.run_elevator(0, 5)
    building.run_elevator(1, -5)
    print("FIRE ALARM!")
    building.fire_alarm()

