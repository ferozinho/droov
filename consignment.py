from enum import Enum
import uuid
import datetime
import random
class ConsignmentStatus(Enum):
    ORDER_PLACED = "order_placed"
    ORDER_ASSIGNED = "order_assigned"
    ORDER_PICKED = "order_picked"
    ORDER_DISPATCHED = "order_dispatched"
    ORDER_DELIVERED = "order_delivered"

class Consignment:
    def __init__(self, c_details:dict = None):
        self.c_id: int = uuid.uuid4()
        self.c_details : dict | None = c_details
        self.status : ConsignmentStatus = ConsignmentStatus.ORDER_PLACED
        self.created_at : datetime = datetime.datetime.now()
        self.updated_at : datetime.datetime | None = None
        self.logs : list = [f"order placed at:{self.created_at}"]
        self.is_active : bool = True
        self.is_assigned_to: int = None
        self.origin = {"x": random.randint(10,99),"y": random.randint(10,99)}
        self.destination = {"x": random.randint(10,99),"y": random.randint(10,99)}
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"

class ConsignmentQueue:
    MAX_LENGTH = 100
    def __init__(self):
        self.queue = []
        self.top = -1

    def isEmpty(self):
        return self.top==-1
    
    def isFull(self):
        return self.top==self.MAX_LENGTH-1
    
    def bulk_enqueue(self,c_list):
        list_size = len(c_list)
        if self.top+list_size == self.MAX_LENGTH-1:
            print(f"overflow.. you can only fill {self.MAX_LENGTH-self.top-2}")
            return
        self.queue.extend(c_list)
        self.top+=list_size
        print(f"enqueued {list_size} consignments")

    def enqueue(self,consignment:int):
        if self.isFull():
            print("overflow")
            return
        self.queue.append(consignment)
        self.top+=1
        print(f"enqueued {consignment}")

    def dequeue(self):
        if self.isEmpty():
            print("underflow")
            return
        dequeued_assignment = self.queue.pop(0)
        self.top-=1
        return dequeued_assignment
    
    def peek(self):
        if self.isEmpty():
            print("underflow")
            return
        return self.queue[0]
    
    def display(self):
        if self.isEmpty():
            print("underflow")
            return
        for i in range(0,self.top):
            print(self.queue[i])
    
def get_consignments(size:int):
    consignments = {}
    for i in range(1,size+1):
        consignment = Consignment()
        consignments[consignment.c_id]=consignment
    return consignments
