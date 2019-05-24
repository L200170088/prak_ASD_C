#Nomor04
class Queue(object):
    def __init__(self):
        self.qlist = []
    def is_Empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_Empty(), "Antrian sedang kosong."
        return self.qlist.pop(0)
    def get_front_most(self):
        assert not self.is_Empty(), "Antrian sedang kosong."
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_Empty(), "Antrian sedang kosong"
        return self.qlist[-1]
    

q = Queue()
q.enqueue(28)
q.enqueue(19)
q.enqueue(14)
q.enqueue(89)

print (q.dequeue())
print (q.dequeue())

print (q.get_front_most())
print (q.get_rear_most())
