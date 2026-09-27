"""

linked lists are always running O(1) average time 
we need a beginning dummy and end dummy

dic to find the location 

dummy -> 1 -> 2 -> 3 -> 4 -> dummy


"""

class ListNode:
    def __init__(self, next=None, prev=None, key=None, val=None):
        self.next = next
        self.prev = prev
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loc = {} # key -> node

        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node) -> None: # always new
        left_node = self.right.prev
        left_node.next = node
        node.prev = left_node
        node.next = self.right
        self.right.prev = node

    def remove(self, node) -> None:
        left_node = node.prev
        right_node = node.next
        left_node.next = right_node
        right_node.prev = left_node
        
    def get(self, key: int) -> int:
        if key not in self.loc:
            return -1
        
        self.remove(self.loc[key])
        self.insert(self.loc[key])
        return self.loc[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.loc:
            self.remove(self.loc[key])
            self.insert(self.loc[key])
            self.loc[key].val = value
        else:
            new_node = ListNode(key=key, val=value)
            self.insert(new_node)
            self.loc[key] = new_node
            if len(self.loc) > self.capacity:
                del_node = self.left.next
                del self.loc[del_node.key]
                self.remove(del_node)


        
