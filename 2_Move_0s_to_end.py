# You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

# Examples:
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]

# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]

class Solution:
    def pushZerosToEnd(self,arr):
        n=len(arr)
        j=0
        
        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[j]=arr[j], arr[i]
                j +=1
        return arr
     
sol=Solution()
arr=[1, 2, 0, 4, 3, 0, 5, 0]
print(sol.pushZerosToEnd(arr))

# not used result=[], because of compiler