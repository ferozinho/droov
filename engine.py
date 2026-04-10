from driver import get_drivers
from consignment import get_consignments
import math
from consignment import ConsignmentQueue
class Engine:
    drivers = get_drivers(50)
    consignments = get_consignments(50)
    c_queue = ConsignmentQueue()
    c_queue.bulk_enqueue(consignments)
    consignment = c_queue.dequeue()
    cords = consignment.origin
    nearest_driver_dist = 100
    driver_assigned = None
    for i in drivers:
        driver_dist = math.sqrt(
            ((cords["x"]-i.cords["x"])**2)+
            ((cords["y"]-i.cords["y"])**2)
            )
        if nearest_driver_dist > driver_dist:
            nearest_driver_dist = driver_dist
            driver_assigned = i
    print(consignment)
    print(nearest_driver_dist)
    print(driver_assigned)
engine = Engine()
print(engine)

