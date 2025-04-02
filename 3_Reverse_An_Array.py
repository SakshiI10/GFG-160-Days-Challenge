# ou are given an array of integers arr[]. Your task is to reverse the given array.

# Examples:
# Input: arr = [1, 4, 3, 2, 6, 5]
# Output: [5, 6, 2, 3, 4, 1]

class Solution:
    def reverseArray(self, arr):
        n=len(arr)
        i=0
        
        while i < n//2:
            arr[i], arr[n-1-i]=arr[n-1-i], arr[i]
            i += 1
            
        return arr
    
sol=Solution()
arr = [1, 4, 3, 2, 6, 5]
print(sol.reverseArray(arr))