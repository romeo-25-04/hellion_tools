from src.systems import System, Planet
from src.orbit import Coordinates


first_planet = Planet("First", Coordinates(1, 2, 3, 4, 5, 6))
second_planet = Planet("Second", Coordinates(11, 12, 13, 14, 15, 16))

arthnar = System(name="arthnar",
                 coordinates=Coordinates(7, 8, 9, 10, 11, 12),
                 planets={1: first_planet,
                       2: second_planet})

print(arthnar.to_json())

with open("var/hellion_system.json", "w") as fl:
    fl.write(arthnar.to_json())

