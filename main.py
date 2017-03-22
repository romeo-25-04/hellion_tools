from src.systems import System, Planet, Asteroid
from src.orbit import Coordinates
from src.building import Module, Port

first_planet = Planet("Tasciana", Coordinates(1, 2, 3, 4, 5, 6))
second_planet = Planet("Hillariath", Coordinates(11, 12, 13, 14, 15, 16))
asterroid = Asteroid("Asterroid_ABC123")
asterroid.coordinates = Coordinates(4, 5, 6, 9, 9, 9)
first_planet.add_object(asterroid)

arthnar = System(name="Arthnar",
                 coordinates=Coordinates(7, 8, 9, 10, 11, 12))

arthnar.add_object(first_planet)
arthnar.add_object(second_planet)

# print(arthnar.objects["Tasciana"].objects["Asterroid_ABC123"].coordinates.first)

# print(arthnar.objects)

# Construct a module
starter_module = Module(name="Ship_27BCBC0")
starter_module.description = "Starting Command Module"
starter_module.add_port(Port.standard)
starter_module.add_port(Port.standard)
starter_module.coordinates.first = 55
# add it to asteroid
asterroid.add_object(starter_module)

with open("var/hellion_system.json", "w") as fl:
    fl.write(arthnar.to_json())

