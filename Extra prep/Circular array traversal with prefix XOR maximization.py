"""
You are given an array ARR which has N integers.
You want to construct a new array RES using ARR by following algo:
1. Initially, RES is empty
2. Start at any index of ARR
3. Choose direction(left or right and iterate over the elements
of ARR starting from the chosen index in the chosen direction)
4. Add each iteration element to the end of the RES
Additionally, it is given that the array is cyclic.
This means that after the last element you will iterate to the 
first one and vice versa.
The value of RES is the sum of the bitwise XOR value of all prefixes.
That means that the value of RES can be defined as follows:
value(RES) = RES[0] + (RES[0]^RES[1]).... + (RES[0]^RES[1]^...RES[N-1])
Find the maximum possible value of RES

Example:
I/p: N=10, ARR = [7,8,5,5,9,2,2,0,1,6]
O/p: 99
"""


class Solution:
    def circularXOR(self, arr):
        n = len(arr)
        max_val = 0

        for start in range(n):
                res_clock = [arr[(start+i) % n] for i in range(n)]
                res_anticlock = [arr[(start-i) % n] for i in range(n)]
                ans = 0
                total = 0
                for i in res_clock:
                     ans ^= i
                     total += ans
                max_val = max(max_val, total)
                ans = 0
                total = 0
                for i in res_anticlock:
                     ans ^= i
                     total += ans
                max_val = max(max_val, total)
            
                

        return max_val
    
solution = Solution()
arr = [7, 8, 5, 5, 9, 2, 2, 0, 1, 6]
print(solution.circularXOR(arr))