# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

from typing import List

class Solution:
    def single_number(self, nums: List[int]) -> int:
        hash_set = {}
        for n in nums:
            if n in hash_set:
                hash_set.pop(n)
            else:
                hash_set[n] = 1
        
        return next(iter(hash_set))
    

# Example 1
print(Solution().singleNumber([2, 2, 1]))  # Output: 1

# Example 2
print(Solution().singleNumber([4, 1, 2, 1, 2]))  # Output: 4

# Example 3
print(Solution().singleNumber([1]))  # Output: 1