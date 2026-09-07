class ListNode:

     def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node   


class LinkedList:
    
    def __init__(self):
        self.ghost_head = ListNode(-1)
        self.tail = self.ghost_head
    
    def get(self, index: int) -> int:
        curr = self.ghost_head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            i +=1
            curr =  curr.next
        return -1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.ghost_head.next
        self.ghost_head.next = new_node
        if not new_node.next:
            self.tail = new_node        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.ghost_head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr #replace tail with the node before tail
            curr.next = curr.next.next
            return True
        return False
            

    def getValues(self) -> List[int]:
        curr = self.ghost_head.next
        res = []
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
        
