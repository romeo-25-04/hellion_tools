from src.systems import System, Planet, Asteroid
from src.orbit import Coordinates


first_planet = Planet("Tasciana", Coordinates(1, 2, 3, 4, 5, 6))
second_planet = Planet("Hillariath", Coordinates(11, 12, 13, 14, 15, 16))
asterroid = Asteroid("Asterroid_ABC123")
first_planet.add_object(asterroid)

arthnar = System(name="Arthnar",
                 coordinates=Coordinates(7, 8, 9, 10, 11, 12))

arthnar.add_object(first_planet)
arthnar.add_object(second_planet)

# print(arthnar.objects["Tasciana"].objects["Asterroid_ABC123"].coordinates.first)

# print(arthnar.objects)

print(arthnar.DESCRIPTION)
print(asterroid.DESCRIPTION)


print(arthnar.to_json())

first_planet.del_object_by_name("Asterroid_ABC")

print(arthnar.to_json())

with open("var/hellion_system.json", "w") as fl:
    fl.write(arthnar.to_json())

