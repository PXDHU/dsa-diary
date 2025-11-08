class Solution(object):
    def mergeAlternatively(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i, j = 0, 0

        res = []

        while i < len(word1) and j < len(word2):   # traverse through the elements until one is over and append alternatively
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1

        res.append(word1[i:])   # append the rest of the elements 
        res.append(word2[j:])
            
        
        return "".join(res)
    
user_input = input(" Enter word1 and word 2 in comma seperated:").strip()
word1, word2 = map(str, user_input.split(", "))

solution = Solution()

result = solution.mergeAlternatively(word1, word2)

print(result)