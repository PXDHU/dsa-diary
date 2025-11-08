class Solution(object):
    def mergeSortArr(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype No returning
        """
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m-=1
            else:
                nums1[last] = nums2[n - 1]
                n-=1
            
            last-=1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n-=1
            last-=1

userInputnums1 = input("Enter nums1 seperated by commas: ")
nums1 = list(map(int, userInputnums1.split(", ")))
m = int(input("Enter m: ")) 
userInputnums2 = input("Enter nums2 seperated by commas: ")
nums2 = list(map(int, userInputnums2.split(", ")))
n = int(input("Enter n: "))

solution = Solution()

print(solution.mergeSortArr(nums1, m, nums2, n))
