"""
Here we should replace all the unique elements in the first places and rest isn't bothered

and return the number of unique elements
"""

class Solution(object):
    def RemoveDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        IndexForNextNumber = 1 # 1 index as the 0th has first unique element

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                nums[IndexForNextNumber] = nums[i]
                IndexForNextNumber+=1
            
        return IndexForNextNumber
    

userInput = input("Enter the elements in array seperated by space: ").strip()
nums = list(map(int, userInput.split(" ")))

solution = Solution()
print(solution.RemoveDuplicates(nums))

print(nums)