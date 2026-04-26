# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/
# Easy
# O(1) average time, O(n) space, where n is the number of keys in the hash set
# Hash Map, Linked List
# We can use an array of linked lists to implement the hash set. The array will have
# a fixed size (e.g., 10^4) and each index will correspond to a bucket. We will use 
# the modulo operator to determine which bucket a key belongs to. Each bucket will be 
# a linked list that stores the keys that hash to that bucket. When we add a key, we 
# will check if it already exists in the corresponding linked list and add it if it 
# does not. When we remove a key, we will search for it in the linked list and remove 
# it if it exists. When we check if a key exists, we will search for it in the linked 
# list and return true if it is found and false otherwise.

class ListNode:
    def __init__(self, key=0, next=None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        trav = self.set[key % len(self.set)]
        while trav.next:
            if trav.next.key == key:
                return
            trav = trav.next
        
        trav.next = ListNode(key)


    def remove(self, key: int) -> None:
        trav = self.set[key % len(self.set)]

        while trav.next:
            if trav.next.key == key:
                trav.next = trav.next.next
                return
            trav = trav.next

    def contains(self, key: int) -> bool:
        trav = self.set[key % len(self.set)] # To get head of index
        
        while trav.next:
            if trav.next.key == key:
                return True
            trav = trav.next
        
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)