from typing import List

class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        
class HashSet():
    def __init__(self):
        self.set = [None for _ in range(10**5)]
        
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
    def contains_duplicate(self, nums: List[int]) -> bool:
        duplicate = HashSet()
        for n in nums:
            if duplicate.get(n):
                return True
            else:
                duplicate.add(n)
            
        return False