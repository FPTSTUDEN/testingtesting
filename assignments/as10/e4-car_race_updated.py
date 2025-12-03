# from pathlib import Path
# import runpy

# module_path = Path(__file__).parent.parent / "as9" / "e4-car_race.py"
# ns = runpy.run_path(str(module_path))
# for name, obj in ns.items():
#     if not name.startswith("_") and callable(obj):
#         globals()[name] = obj
try:
    from testingtesting.assignments.as9.e123 import Car
except ImportError:
    import sys, os
    # add parent of the "testingtesting" package to sys.path so the absolute import works
    package_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    if package_root not in sys.path:
        sys.path.insert(0, package_root)
    from testingtesting.assignments.as9.e123 import Car
import random
class Race():
    def __init__(self, name, distance, *cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
    def print_status(self):
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.speed:3.0f} km/h  {car.traveled_distance:6.1f} km")
            #format registration number left-aligned in a field of width 10
            #format speed right-aligned in a field of width 3 with no decimal places
            #format traveled distance right-aligned in a field of width 6 with 1 decimal place
    def race_finished(self):
        for car in self.cars:
            if car.traveled_distance >= self.distance:
                return True
        return False
if __name__ == "__main__":
    car_list = []
    for i in range(10):
        #reg_number = f"CAR-{i+1:03d}"
        reg_number = f"ABC-{i+1}"
        max_speed = random.randint(100, 200)
        car_list.append(Car(reg_number, max_speed))
    #cars = {car.registration_number: car for car in car_list}
    race = Race("Grand Demolition Derby", 8000, *car_list)
    hours = 0
    while not race.race_finished():
        race.hour_passes()
        if hours % 10 == 0:
            print(f"--- Hour {hours} ---")
            race.print_status()
        hours += 1
    print(f"Race finished in {hours} hours.")
    race.print_status()