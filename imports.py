import time
import pytest
from classes import Motorcycle, Car

print(Motorcycle)

moto = Motorcycle('Test', 'Tester')
car = Car('Honda', 'Civic')

for vehicle in [car, moto]:
    print(f'The time is {time.time()}')
    print(vehicle)
    print(vehicle.is_engine_on)
    vehicle.turn_engine_on()
    print(vehicle.is_engine_on)
    vehicle.turn_engine_on()
    vehicle.turn_headlight_on()
    vehicle.start_driving()
    vehicle.turn('left')
    vehicle.turn('right')
    vehicle.stop_driving()
    vehicle.turn_engine_off()
    vehicle.turn_headlight_off()
    print()
    time.sleep(1)