from enum import Enum
import uuid
import datetime
import json
import random

class DriverStatus(Enum):
    AVAILABLE = "available"
    BUSY_PICKING = "busy_picking"
    PICKED = "picked"
    BUSY_DELIVERING = "busy_delivering"
    UNAVAILABLE = "unavailable"

class Driver:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self.status : DriverStatus = DriverStatus.AVAILABLE
        self.is_active = True
        self.cords = {"x": random.randint(10,99),"y": random.randint(10,99)}
        self.consignments = []
    
    @property
    def is_occupied(self):
        return len(self.consignments) == 2

    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"
    
def get_drivers(size:int):
    drivers = {}
    for i in range(1,size-1):
        driver = Driver(f"driver{i}",i)
        drivers[driver.id] = driver
    return drivers