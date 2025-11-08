class Solution(object):
    def ValidPalidromeii(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l , r = 0, len(s)-1

        while l < r:    #same as the valid palidrome 1
         if s[l] != s[r]:
            skipL, skipR = s[l+1:r+1], s[l:r]   # we are skipping the left and right pointer 
            return(skipL == skipL[::-1] or skipR == skipR[::-1])    # if the any pointer skipped is equal to the reverse version of itself
         l+=1
         r-=1
         
        return True

            
            
        

user_Input = input("Enter the string: ").strip()
s = str(user_Input)

solution = Solution()

print(solution.ValidPalidromeii(s))