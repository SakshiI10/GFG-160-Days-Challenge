# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Examples :
# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]

class Solution:
    def rotateArr(self, arr, d):
        n=len(arr)
        d=d%n
        
        arr[:]=arr[d:]+arr[:d]
        return arr
    
sol=Solution()
arr = [1, 2, 3, 4, 5]
d = 2
print(sol.rotateArr(arr, d))