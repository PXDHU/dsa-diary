"""
You are given an integer n. A 0-indexed integer array nums of length n+1 is generated following the rules
1. nums[0]=0
2. nums[1]=1
3. nums[2*i]= nums[i], when 2 <= 2*i <= n
4. nums[(2*i)+1]= nums[i] + nums[i+1], when 2 <= 2*i+1 <= n
Return the maximum integer in the arrays nums.

""" 
class Solution:
    def maxInteger(self, n):
        if n == 0:
            return 0
        
        arr = [0] * (n+1)
        arr[0] = 0
        arr[1] = 1

        for i in range(1, (n//2) + 1):
            if 2*i <= n:
                arr[2*i] = arr[i]
            if 2*i+1 <=n :
                arr[2*i +1] = arr[i] + arr[i+1]

        return arr, max(arr)

solution = Solution()

n = int(input("Enter the number: "))

result = solution.maxInteger(n)

print(result)