class Solution(object):
    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()

        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return True
        
        return False
    
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = set()

        for num in nums:
            if num in dup:
                return True
            dup.add(num)

        return False
    
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(list(set(nums))) != len(nums)
    
user_input = input("Enter array elements seperated by spaces: ").strip()
nums = list(map(int, user_input.split(' ')))

solution = Solution()

result_1 = solution.containsDuplicate(nums)
result_2 = solution.containsDuplicate1(nums)
result_3 = solution.containsDuplicate2(nums)

print("Output:")
print("Result method 1:", result_1)
print("Result method 2:", result_2)
print("Result method 3:", result_3)
    