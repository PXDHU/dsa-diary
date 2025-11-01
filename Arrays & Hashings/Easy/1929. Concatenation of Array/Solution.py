class Solution(object):
    def getConcatenation1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        """
        n = len(nums)

        ans = [0] * (2*n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums [i]

        return ans
    
    def getConcatenation2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        """

        return nums+nums
    
user_input = input("Enter array elements seperated by space: ").strip()
nums = list(map(int, user_input.split(' ')))

solution = Solution()
result1 = solution.getConcatenation1(nums)
result2 = solution.getConcatenation2(nums)

print("Output:")
print("Result method 1: ", result1)
print("Result method 2: ", result2)