from src.systems import SpaceObject
"""
inheritance
SpaceObject <-- Station
Station <-- Module
Station <-- Ship
Staton <-- Arena
"""

class Port:
    airlock = "Airlock Port"
    standard = "Standard Port"
    cargo_door = "Cargo Door"
    grappling = "Grappling Port"


class StationTypes:
    building = "Building module"
    ship = "Ship"
    arrena = "PvP Arrena with lots of parts"


class Station(SpaceObject):
    def __init__(self, name):
        SpaceObject.__init__(self, name)
        self.ports = []
        self.description = "default"

    def add_port(self, port):
        self.ports.append(port)


class Module(Station):
    DESCRIPTION = StationTypes.building

    def __init__(self, name):
        Station.__init__(self, name)
        self.description = StationTypes.building


class Ship(Station):
    DESCRIPTION = StationTypes.ship


class Arena(Station):
    DESCRIPTION = StationTypes.arrena
