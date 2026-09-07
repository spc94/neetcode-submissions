# Double linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    
    def __init__(self):
        self.ghost_head = Node(-1)
        self.ghost_tail = Node(-1)
        self.ghost_head.next = self.ghost_tail
        self.ghost_tail.prev = self.ghost_head        


    def isEmpty(self) -> bool:
        return self.ghost_head.next == self.ghost_tail
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        current_last_node = self.ghost_tail.prev

        current_last_node.next = new_node
        new_node.prev = current_last_node

        new_node.next = self.ghost_tail
        self.ghost_tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        current_first_node = self.ghost_head.next

        current_first_node.prev = new_node
        new_node.next = current_first_node

        new_node.prev = self.ghost_head
        self.ghost_head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.ghost_tail.prev
        value = last_node.value
        prev_node = last_node.prev

        prev_node.next = self.ghost_tail
        self.ghost_tail.prev = prev_node
        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.ghost_head.next
        value = first_node.value
        following_node = first_node.next

        following_node.prev = self.ghost_head
        self.ghost_head.next = following_node
        return value
