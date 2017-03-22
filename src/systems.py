from src.orbit import Coordinates
import json


class Planet:
    def __init__(self, name, coordinates=Coordinates):
        self.name = name
        self.coordinates = coordinates


class System:
    def __init__(self, name, coordinates=Coordinates, planets={}):
        self.name = name
        self.coordinates = coordinates
        self.planets = planets

    def add_planet(self, planet):
        self.planets[planet.name] = planet

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True, indent=2)
