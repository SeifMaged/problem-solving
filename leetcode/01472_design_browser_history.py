# Medium
# Design - Doubly Linked List
# O(1) Time for visit, O(steps) Time for back and forward, where steps is the number of steps to move back or forward.
# O(n) Space, where n is the number of URLs visited. We use a doubly linked list to store the browsing history, which allows us to efficiently move back and forward through the history.

class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(val=homepage)

    def visit(self, url: str) -> None:
        self.current.next = ListNode(val=url, prev = self.current)
        self.current = self.current.next
        

    def back(self, steps: int) -> str:
        trav = self.current

        while trav.prev and steps:
            trav = trav.prev
            steps -= 1
        
        self.current = trav
        return trav.val

    def forward(self, steps: int) -> str:
        trav = self.current

        while trav.next and steps:
            trav = trav.next
            steps -= 1
        
        self.current = trav
        return trav.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)