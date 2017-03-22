from src.orbit import Coordinates
import json
"""
name is what u see on the map
"""


class SpaceObject:
    def __init__(self, name, coordinates=Coordinates()):
        self.name = name
        self.coordinates = coordinates
        self.objects = {}

    def add_object(self, obj):
        self.objects[obj.name] = obj

    def del_object_by_name(self, name):
        if name in self.objects:
            del self.objects[name]

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True, indent=2)


class System(SpaceObject):
    DESCRIPTION = "Main Star"


class Planet(SpaceObject):
    DESCRIPTION = "In orbit of a Star"


class Asteroid(SpaceObject):
    DESCRIPTION = "In orbit of a Planet"
