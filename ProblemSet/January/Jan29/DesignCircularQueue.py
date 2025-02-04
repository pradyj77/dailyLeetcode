class MyCircularDeque:

    def __init__(self, k: int):
        self.myCircularQueue = []
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        #print(self.myCircularQueue)
        if len(self.myCircularQueue) < self.maxSize:
            self.myCircularQueue.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        #print(self.myCircularQueue)
        if len(self.myCircularQueue) < self.maxSize:
            self.myCircularQueue.append(value)
            return True
        return False      

    def deleteFront(self) -> bool:
        if len(self.myCircularQueue) > 0:
            self.myCircularQueue.pop(0)
            return True
        return False
        
    def deleteLast(self) -> bool:
        if len(self.myCircularQueue) > 0:
            self.myCircularQueue.pop(-1)
            return True
        return False

    def getFront(self) -> int:
        if len(self.myCircularQueue) > 0:
            return self.myCircularQueue[0]
        return -1
        

    def getRear(self) -> int:
        #print(self.myCircularQueue)
        if len(self.myCircularQueue) > 0:
            return self.myCircularQueue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.myCircularQueue) == 0

    def isFull(self) -> bool:
        return len(self.myCircularQueue) == self.maxSize


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()