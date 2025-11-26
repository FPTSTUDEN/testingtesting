class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.traveled_distance = 0
    def accelerate(self, speed_increase):
        self.speed += speed_increase
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < 0:
            self.speed = 0
    def drive(self, hours):
        self.traveled_distance += self.speed * hours

if __name__ == "__main__":
    car = Car("ABC-123", 142)
    for property, value in vars(car).items():
        print(f"{property}: {value}")
    for speed in (30, 70, 50):
        car.accelerate(speed)
    print(f"Current speed: {car.speed} km/h")
    car.accelerate(-200)
    print(f"Current speed after braking: {car.speed} km/h")