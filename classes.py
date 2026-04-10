from enum import Enum
import uuid
import datetime
import json
class ConsignmentStatus(Enum):
    ORDER_PLACED = "order_placed"
    ORDER_ASSIGNED = "order_assigned"
    ORDER_PICKED = "order_picked"
    ORDER_DISPATCHED = "order_dispatched"
    ORDER_DELIVERED = "order_delivered"

class Consignment:
    def __init__(self, c_details:json = None):
        self.c_id = uuid.uuid4()
        self.c_details = c_details
        self.status = ConsignmentStatus.ORDER_PLACED
        self.created_at = datetime.datetime.now()
        self.updated_at = None
        self.logs = [f"order placed at:{self.created_at}"]
        self.is_active = True
        
    def __repr__(self):
        return f"id:{self.c_id}"

class Driver:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
        self.is_active = True
    def __repr__(self):
        return (f"Name: {self.name}, id: {self.id},is_active: {self.is_active}")
    
def get_drivers(size:int):
    drivers = []
    for i in range(0,size):
        drivers.append(Driver(f"driver{i}",i))
    return drivers

def get_consignments(size:int):
    consignments = []
    for i in range(0,size):
        consignments.append(Consignment())
    return consignments