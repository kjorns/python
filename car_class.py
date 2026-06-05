# 10/08/2025
# CAR CLASS

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # This getter method for reading the year and model of the car
    def get_year_model(self):
        return self.__year_model

    # This getter method for reading the make of the car
    def get_make(self):
        return self.__make

    # This method makes the car go faster, adds 5 speed
    def accelerate(self):
        self.__speed += 5

    # This method makes the car go slower, subtracts 5 speed
    def brake(self):
        self.__speed -= 5

    # This getter method tells us the current speed of the car
    def get_speed(self):
        return self.__speed

def main():
    # Make a new car object
    car_year_model = "2021 Civic"
    car_make = "Honda"
    my_car = Car(car_year_model, car_make)

    # Print the cars information
    print(f"Year Model: {my_car.get_year_model()}")
    print(f"Make: {my_car.get_make()}")
    print(f"Initial Speed: {my_car.get_speed()} mph")

    # Make the car accelerate 5 times
    print("Accelerating...")
    
    for i in range(5):
        my_car.accelerate()
        
        current_speed = my_car.get_speed()
        print(f"{i + 1}: Speed went up! Current Speed is {current_speed} mph")

    # Make the car break 5 times
    print("Braking...")
    
    for i in range(5):
        my_car.brake()
        
        current_speed = my_car.get_speed()
        print(f"{i + 1}: Speed went down! Current Speed is {current_speed} mph")

# Call the main function
if __name__ == "__main__":
    main()