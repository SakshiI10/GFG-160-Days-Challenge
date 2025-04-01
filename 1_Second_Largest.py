# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Examples:
# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34

class Solution:
    def getSecondLargest(self, arr):
        res=set(arr)
        
        if len(res)<2:
            return -1
            
        res.remove(max(res))
        return max(res)
    
sol=Solution()
arr=[12, 35, 1, 10, 34, 1]
print(sol.getSecondLargest(arr))