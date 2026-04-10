from classes import get_consignments,get_drivers,Consignment
class ConsignmentQueue:
    MAX_LENGTH = 100
    def __init__(self):
        self.queue = []
        self.top = -1

    def isEmpty(self):
        return self.top==-1
    
    def isFull(self):
        return self.top==self.MAX_LENGTH-1
    
    def bulk_enqueue(self,c_list:list[Consignment]):
        list_size = len(c_list)
        if self.top+list_size == self.MAX_LENGTH-1:
            print(f"overflow.. you can only fill {self.MAX_LENGTH-self.top-2}")
            return
        self.queue.extend(c_list)
        self.top+=list_size
        print(f"enqueued {list_size} consignments")

    def enqueue(self,consignment:Consignment):
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
        top-=1
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
    

class Engine:
    drivers = get_drivers(50)
    consignments = get_consignments(50)
    c_queue = ConsignmentQueue()
    c_queue.bulk_enqueue(consignments)

engine = Engine()
print(engine)

