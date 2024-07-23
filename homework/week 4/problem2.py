class Car:
    def __init__(self, color, speed, max_passengers, passengers):
        self.color = color
        self.color = color
        self.speed = speed
        self.max_passengers = max_passengers
        self.passengers = passengers

    def get_color(self):
        return self.color
    
    def get_distance_traveled(self, time):
        return self.speed*time
    
    def add_passenger(self):
        if self.passengers < self.max_passengers:
            self.passengers += 1
        else:
            print("already at max passengers")
    
    def remove_passenger(self):
        if self.passengers > 0:
            self.passengers -= 1

def test(input, expected, msg):
    if input == expected:
        print(msg, "passed")
    else:
        print(msg, "failed")

car = Car("red", 60, 4, 2)

test(car.get_color(), "red", "1")
test(car.get_distance_traveled(5), 300, "2")
test(car.get_distance_traveled(4.3), 258, "3")

print("\ntest 4")
car.add_passenger()
car.add_passenger()
print("number of passengers:", car.passengers)
car.add_passenger()
print("number of passengers:", car.passengers)

print("\ntest 5")
car.remove_passenger()
car.remove_passenger()
car.remove_passenger()
car.remove_passenger()
print("number of passengers:", car.passengers)
car.remove_passenger()
print("number of passengers:", car.passengers)
