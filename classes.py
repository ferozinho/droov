from enum import Enum
import uuid
import datetime
import json
import random
class ConsignmentStatus(Enum):
    ORDER_PLACED = "order_placed"
    ORDER_ASSIGNED = "order_assigned"
    ORDER_PICKED = "order_picked"
    ORDER_DISPATCHED = "order_dispatched"
    ORDER_DELIVERED = "order_delivered"

class DriverStatus(Enum):
    AVAILABLE = "available"
    DELIVERING = "delivering"
    UNAVAILABLE = "unavailable"

class Consignment:
    def __init__(self, c_details:dict = None):
        self.c_id: int = uuid.uuid4()
        self.c_details : dict | None = c_details
        self.status : ConsignmentStatus = ConsignmentStatus.ORDER_PLACED
        self.created_at : datetime = datetime.datetime.now()
        self.updated_at : datetime.datetime | None = None
        self.logs : list = [f"order placed at:{self.created_at}"]
        self.is_active : bool = True
        self.origin = {"x": random.randint(10,99),"y": random.randint(10,99)}
        self.destination = {"x": random.randint(10,99),"y": random.randint(10,99)}
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

class Driver:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self.status : DriverStatus = DriverStatus.AVAILABLE
        self.is_active = True
        self.cords = {"x": random.randint(10,99),"y": random.randint(10,99)}
        
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"
    
def get_drivers(size:int):
    drivers = []
    for i in range(1,size-1):
        drivers.append(Driver(f"driver{i}",i))
    return drivers

def get_consignments(size:int):
    consignments = []
    for i in range(1,size-1):
        consignments.append(Consignment())
    return consignments

consignment = Consignment()
print(consignment)