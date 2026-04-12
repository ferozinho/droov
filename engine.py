from driver import get_drivers
from consignment import get_consignments
import math
from consignment import ConsignmentStatus,Consignment,ConsignmentQueue
from driver import Driver,DriverStatus
import datetime
import uuid
class Engine:
    def __init__(self):
        self.db = None

    def fetch_data(self,d_len,c_len):
        drivers = get_drivers(d_len)
        consignments = get_consignments(c_len)
        return drivers,consignments

    def temp_db(self):
        self.db =  {
            "drivers":None,
            "consignments":None
        }

    def find_nearest_driver(self,consignment:Consignment)->int:
        c_x,c_y = consignment.origin["x"],consignment.origin["y"]
        nearest_driver_dist = 100
        drivers = self.db["drivers"]
        driver_assigned = None
        for k,v in drivers.items():
            if not v.status == DriverStatus.AVAILABLE:
                continue
            driver = v
            d_x,d_y = driver.cords["x"],driver.cords["y"]
            driver_dist = math.sqrt(((c_x - d_x)**2)+(( c_y-d_y )**2))
            if nearest_driver_dist > driver_dist:
                nearest_driver_dist = driver_dist
                driver_assigned = k
        print("nearest_driver: ",driver_assigned)
        return driver_assigned

    def assign_consignment(self,c_queue:ConsignmentQueue):
        consignments = self.db["consignments"]
        drivers = self.db["drivers"]
        c_id = c_queue.dequeue()
        print(c_id)
        consignment = consignments[c_id]
        d_id = self.find_nearest_driver(consignment)
        assigned_driver = drivers[d_id]
        consignment.status = ConsignmentStatus.ORDER_ASSIGNED
        consignment.updated_at = datetime.datetime.now()
        consignment.logs.append(f"Consignment id:{consignment.c_id} has been assigned to {assigned_driver.name} at {consignment.updated_at}")
        consignment.assigned_to = d_id
        assigned_driver.status = DriverStatus.BUSY_PICKING
        assigned_driver.consignments.append(c_id)
        return c_id

    def pick_consignment(self,c_id,is_multiple=False):
        consignments = self.db["consignments"]
        consignment = consignments[c_id]
        driver = self.db["drivers"][consignment.assigned_to]
        consignment.status = ConsignmentStatus.ORDER_PICKED
        consignment.updated_at = datetime.datetime.now()
        consignment.logs.append(f"Consignment id:{consignment.c_id} has been picked by {driver.name} at {consignment.updated_at}")
        if not is_multiple:
            driver.status = DriverStatus.PICKED
        
    def start_delivery_process(self,c_id:int):
        consignments = self.db["consignments"]
        consignment = consignments[c_id]
        driver = self.db["drivers"][consignment.assigned_to]
        consignment.status = ConsignmentStatus.ORDER_DISPATCHED
        consignment.updated_at = datetime.datetime.now()
        consignment.logs.append(f"Consignment id:{consignment.c_id} is being dispatched by {driver.name} at {consignment.updated_at}")
        driver.status = DriverStatus.BUSY_DELIVERING
    
    def finish_delivery(self,c_id:int,is_multiple=False):
        consignments = self.db["consignments"]
        consignment = consignments[c_id]
        driver = self.db["drivers"][consignment.assigned_to]
        consignment.status = ConsignmentStatus.ORDER_DELIVERED
        consignment.updated_at = datetime.datetime.now()
        consignment.logs.append(f"Consignment id:{consignment.c_id} has been delivered by {driver.name} at {consignment.updated_at}")
        print(consignment.logs)
        consignment.is_active = False
        if not is_multiple:
            driver.status = DriverStatus.AVAILABLE

engine = Engine()
epochs = 10
d,c = engine.fetch_data(epochs,epochs)
engine.temp_db()
engine.db["drivers"] = d
engine.db["consignments"] = c
consignments = engine.db["consignments"]
print(consignments)
c_queue = ConsignmentQueue()
for k,v in consignments.items():
    if v.status == ConsignmentStatus.ORDER_PLACED:
        c_queue.enqueue(k)
while c_queue.isEmpty() == False:
    c_id = engine.assign_consignment(c_queue)
    engine.pick_consignment(c_id)
    engine.start_delivery_process(c_id)
    engine.finish_delivery(c_id)








