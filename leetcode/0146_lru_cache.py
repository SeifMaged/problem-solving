# 146. LRU Cache
# leetcode.com/problems/lru-cache/
# Medium
# O(1) time, O(capacity) space, where capacity is the maximum number of items the cache can hold
# Hash Map, Doubly Linked List
# We use a hash map to store the key-value pairs for O(1) access. We also use a doubly linked list to keep track of the order of usage of the items in the cache. The most recently used item is moved to the end of the list, while the least recently used item is at the beginning of the list. When we need to evict an item from the cache, we remove the item at the beginning of the list (the least recently used item) and delete it from the hash map.
# The get and put operations both run in O(1) time because we can access the hash map in O(1) time and we can insert and remove nodes from the doubly linked list in O(1) time. The space complexity is O(capacity) because we are storing at most capacity items in the cache.

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if self.cache.get(key, None):
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, None):
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)