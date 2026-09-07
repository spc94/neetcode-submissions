class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.size = 0
        self.array = [0] * capacity


    def get(self, i: int):
        return self.array[i]

    def set(self, i: int, n: int):
        self.array[i] = n

    def pushback(self, n: int):
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size+=1


    def popback(self):
        self.size-=1
        return self.array[self.size]
        

    def resize(self):
        self.capacity = self.capacity * 2
        #for a contiguous array in memory
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr


    def getSize(self):
        return self.size        
    
    def getCapacity(self):
        return self.capacity
