import random
from e123 import Car
if __name__ == "__main__":
    car_list = []
    for i in range(10):
        #reg_number = f"CAR-{i+1:03d}"
        reg_number = f"ABC-{i+1}"
        max_speed = random.randint(100, 200)
        car_list.append(Car(reg_number, max_speed))
    winner = None
    while winner is None:
        for car in car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.traveled_distance >= 10000:
                print(f"Car {car.registration_number} has won the race!")
                winner = car
                break
    for car in car_list:
        print(f"Car {car.registration_number} traveled {car.traveled_distance} km")
        
