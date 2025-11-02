"""
Interesting Problem !!

So the characters and the number of characters must be equal in both strings.

Traverse and comparing on both list of characters ? That will be O(n^2) :( 

Hash map ? Yes O(n). Let's try that as well

"""

class Solution(object):
    def isAnagram_Hash(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        Count_s, Count_t = {}, {}

        for i in range(len(s)):
            Count_s[s[i]] = 1 + Count_s.get(s[i], 0)
            Count_t[t[i]] = 1 + Count_t.get(t[i], 0)
        
        for c in Count_s:
            if Count_s[c] != Count_t.get(c, 0):
                return False
        return True
    
    """
    But This Hashmap will give us Space complexity problem as Hash map is has varible space

    Let's Try another method with Constant Space complexity
    1. Quick length check - immediate disqualification if lengths differ
    2. Character frequency array - count occurrences of each character
    3. Increment for string s - build frequency profile
    4. Decrement for string t - subtract frequency profile
    5. Validate zero counts - all frequencies must cancel out to zero

    """

    def isAnagram_Arr(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths differ, can't be anagrams
        if len(s) != len(t):
            return False

        # Create an array for 26 lowercase letters
        char_counts = [0] * 26

        # Count characters in s
        for i in range(len(s)):
            char_counts[ord(s[i]) - ord('a')] += 1

        # Subtract counts for t
        for i in range(len(t)):
            char_counts[ord(t[i]) - ord('a')] -= 1

        # Check if all counts are zero
        for count in char_counts:
            if count != 0:
                return False

        return True
    

user_input_1 = input("Enter the First String:")
user_input_2 = input("Enter the Second String:")

s = user_input_1.strip().lower()
t = user_input_2.strip().lower()

solution = Solution()

result_1 = solution.isAnagram_Hash(s, t)
result_2 = solution.isAnagram_Arr(s, t)

print(result_1)

