class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        
class HashSet():
    def __init__(self):
        self.set = [None for n in range(10**5)]
        
    def add(self, key : int) -> None:
        curr = self.set[key % len(self.set)]
        
        if curr == None:
            self.set[key%len(self.set)] = ListNode(key)
            return
        
        while curr:
            if curr.key == key:
                return
            if curr.next == None:
                break
            curr = curr.next
            
        curr.next = ListNode(key)
        return
    
    def get(self, key : int) -> bool :
        curr = self.set[key % len(self.set)]
        if curr == None:
            return False
        
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
            
        return False
        

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = HashSet()
        for n in nums:
            if hash.get(n):
                return True
            else:
                hash.add(n)
            
        return False