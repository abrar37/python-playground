# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car:

    # Problem: Add a class variable to Car that keeps track of the number of cars created.
    total_cars = 0
    def __init__(self, brand, model):
        self.__brand = brand
        # Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
        self.__model = model

        Car.total_cars += 1

    def get_model(self):
        return self.__model + "!"
    
    # Setter for model with validation.
    def set_model(self, new_model):
        if not isinstance(new_model, str):
            raise ValueError("Brand must be a string.")
        self.__model = new_model

    # Problem: Add a method to the Car class that displays the full name of the car (brand and model).
    def fullname(self):
        return(f"{self.__brand}, {self.__model}")
    
    # Problem: Add a class variable to Car that keeps track of the number of cars created.
    def fuel_type(self):
        return "Petrol or Diesel"


    # Problem: Add a static method to the Car class that returns a general description of a car.
    @staticmethod
    def general_description():
        return "Excellence in Motion"
    
    # Problem: Use a property decorator in the Car class to make the brand attribute read-only. 
    @property
    def brand(self):
        return self.__brand

my_car = Car("Toyota", "Corolla")


# print(my_car.brand)

# print(my_car.get_model())

my_car.set_model("camry")
# print(my_car.get_model())

# print(my_car.fuel_type())


# print(Car.general_description())
# print(my_car.general_description())




# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"




ev_car = ElectricCar("Tesla", "Model S", "95kWh")

# print(ev_car.battery_size)
# print(ev_car.fullname())

# ev_car.set_model("Model Y")

# print(ev_car.get_model())

# print(ev_car.fuel_type())

# print(Car.total_cars)


# Problem: Demonstrate the use of isinstance() to check if ev_car is an instance of Car and ElectricCar.
# print(isinstance(ev_car, Car))
# print(isinstance(ev_car, ElectricCar))



# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Battery:
    def battery_info(self):
        return "Battery is here"

class Engine:
    def engine_info(self):
        return "Engine is here"

class ElectricCarTwo(Battery, Engine, Car):
    pass

new_ev_car = ElectricCarTwo("Tesla", "Model Y")

print(new_ev_car.battery_info())
print(new_ev_car.engine_info())
