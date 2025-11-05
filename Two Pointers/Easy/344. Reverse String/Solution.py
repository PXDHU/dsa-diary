class Solution(object):
    def ReverseString(self, s):    # Time Complexity: O(n), Space: O(1)
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # We gonna exchange inplace with two pointers
        l, r = 0, len(s) - 1 # l to leftmost and r to rightmost

        while l < r:    # till l must be less than r, if odd It will be equal but that must not be disturbed
            s[l], s[r] = s[r], s[l] #Exchange

            l+=1    # Increment the left pointer 
            r-=1    #Decrement the right pointer

user_input = input("Enter the string with comma seperated :").strip()
s = list(map(str, user_input.split(',')))

solution = Solution()

solution.ReverseString(s)

print("Reversed String:", s)

