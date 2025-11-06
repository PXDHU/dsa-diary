class Solution(object):
    def ValidPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = ""

        for c in s:
            if c.isalnum(): #Built in string method
                newStr += c.lower()
        
        return newStr == newStr[::-1] #reverse the string
    
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0   # left pointer
        r = len(s) - 1  # right pointer

        while l < r:
            while not self.alnum(s[l]) and l < r:   # if not in alpha numeric, skip that char
                l+=1
            while not self.alnum(s[r]) and r > l:
                r-=1
            
            if s[l].lower() != s[r].lower():    #Compare the lower cases  of both pointers
                return False

            l+=1 # Increment and decrement the pointers
            r-=1
        
        return True

    
    def alnum(self, c): # To check alphanumeric
        return (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
    
user_input = input("Enter the string: ").strip()
s = str(user_input)

solution = Solution()
result1 = solution.ValidPalindrome1(s)
result2 = solution.isPalindrome2(s)

print(result1)
print(result2)