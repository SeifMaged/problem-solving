# Medium
# Linked List
# Complexity Depends on the input but here is the complexity for each function:
# O(n) Time, where n is the number of nodes in the linked list for get, addAtIndex and deleteAtIndex. O(1) Time for addAtHead and addAtTail
# O(1) Space for all functions
class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        else:
            trav = self.head
            while index:
                index -= 1
                trav = trav.next
            return trav.val
        

    def addAtHead(self, val: int) -> None:
        if self.head is None: # Empty List
            self.head = Node(val)
            self.tail = self.head
            self.length += 1
            return

        temp = Node(val=val, next=self.head)
        self.head.prev = temp
        self.head = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.tail is None:
            self.addAtHead(val) # Same case as empty list
            return

        temp = Node(val=val, prev=self.tail)
        self.tail.next = temp
        self.tail = temp
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            pass
        else:
            trav = self.head
            while index:
                index -= 1
                trav = trav.next
            temp = Node(val=val, next=trav, prev=trav.prev)
            if temp.prev:
                temp.prev.next = temp
            trav.prev = temp
            self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        elif index == 0:
            if self.head:
                self.head = self.head.next
                self.length -= 1
        elif index == self.length-1:
            if self.tail:
                self.tail = self.tail.prev
                self.length -= 1
        else:
            trav = self.head
            while index:
                index -= 1
                trav = trav.next
            
            prev = trav.prev
            next = trav.next
            prev.next = next
            if next:
                next.prev = prev
            self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)