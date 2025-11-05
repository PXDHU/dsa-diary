class Solution(object):
    def LongestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        max_len = float('inf')

        i = 0

        for s in strs:
            if len(s) < max_len:
                max_len = len(s)    # The max length of longest common prefix will be the length of the smallest string

        while i < max_len:  # while loop for the chars
            for s in strs:  # for loop for each word
                if s[i] != strs[0][i]:  # compare each word's char to first word char
                    return s[:i]    # if not return the char before

            i+=1    # Increment to the check next char

        return strs[0][:i]  # returning the first word's char till the break of while
    
user_input = input("Enter the strings with comma seperated values: ").strip()
strs = list(map(str, user_input.split(', ')))

solution = Solution()

result = solution.LongestCommonPrefix(strs)

print(result)