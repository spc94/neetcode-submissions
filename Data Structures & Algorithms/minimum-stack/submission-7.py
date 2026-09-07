class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.sorted_stack: # if not check if empty
            self.sorted_stack.append(val)  
        elif val > self.sorted_stack[-1]:
            self.sorted_stack.append(self.sorted_stack[-1])
        else:
            self.sorted_stack.append(val)
        

        
    def pop(self) -> None:
        self.stack.pop()
        self.sorted_stack.pop()
        
        print(self.sorted_stack)
        return
       

    def top(self) -> int:
        return self.stack[-1] # -1 always give the last value of a list in pyrhon

    def getMin(self) -> int:
        return self.sorted_stack[-1]


'''

push 3 push 1 push 2  push -1 
sorted 3 , 1, 1 , -1
min -1
pop -1
>> min 1
pop >> 2
>> 1 


'''
        
