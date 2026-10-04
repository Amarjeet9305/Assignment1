class Car:
    def __init__(self,brand, color,top_speed):
        self.brand = brand
        self.color = color
        self.top_speed = top_speed
        self.current_speed = 0
    # Create a function on behavior/ methods
    
    def accelerate(self): 
        self.current_speed +=20
        print(f"The {self.color} {self.brand} is now moving at {self.current_speed} km/h")


# Function calling or (Creating a object from the class)

car1 = Car("Ferrari","Red", 400)
car2 = Car("BMW","Green",240)        

# using the actions (Methods)
car1.accelerate()
car2.accelerate()