class Vehicle:
    is_engine_on = False
    is_headlight_on = False
    make = None
    model = None
    is_driving = False

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self) :
        return (f'{self.make} {self.model} with engine '
            f'{"on" if self.is_engine_on else "off"}'
            f' and headlight {"on" if self.is_headlight_on else "off"}')

    def turn_engine_on(self): #like reference to the object itself
        print("Turning engine on")
        self.is_engine_on = True

    def turn_engine_off(self): 
        print("Turning engine off")
        if self.is_driving:
            print("You are driving!!!!")
            return
        self.is_engine_on = False

    def turn_headlight_on(self): 
        print("Turning headlight on")
        self.is_headlight_on = True

    def turn_headlight_off(self): 
        print("Turning headlight off")
        self.is_headlight_on = False

    def start_driving(self): 
        if not self.is_engine_on:
            print("You cannot drive without engine on")
        print("Starting to drive...")
        self.is_driving = True

    def stop_driving(self): 
        print("Stopping...")
        self.is_driving = False


class Motorcycle(Vehicle): # all python classes are capitalized
   
    def lean(self, direction):
        if not self.is_driving:
            print("You are not driving!!!")
            return
        print(f'Turning {direction}')

    def turn_handlebars(self, direction):
        print(f'Turning handlebars {direction}')

    def turn(self, direction):
        if direction == 'left':
            self.turn_handlebars('right')
            self.lean('left')
        elif direction == 'right':
            self.turn_handlebars('left')
            self.lean('right')
        else:
            print("Didn't understand direction..")

class Car(Vehicle): # all python classes are capitalized
    def turn_steering_wheel(self, direction):
        print(f'Turning steering wheel {direction}')
    
    def turn(self, direction):
        if direction in ['left', 'right']:
            self.turn_steering_wheel(direction)
        else:
            print("Didn't understand direction..")






