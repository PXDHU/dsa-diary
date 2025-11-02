class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numMap = {}
        n = len(nums)

        for i in range(n): # i = 0 # i = 1
            comp = target - nums[i] # 7 = 9 - 2 # 2 = 9 - 7

            if comp in numMap: # 7 not in Hashmap # 2 in Hashmap
                return [numMap[comp], i] # [0, 1] value/index of 2 and index of 7
            numMap[nums[i]] = i # added 2 -> key value -> 0

        return []
    
user_input = input("Enter the elements in array with space: ").strip()
user_input1 = input("Enter the Target: ").strip()

nums = list(map(int, user_input.split(" ")))
target = int(user_input1)

solution = Solution()
result = solution.twoSum(nums, target)

print(result)