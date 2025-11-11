"""
This is a really interesting problem!

We need to group words that are anagrams into sublists.

We'll use a similar idea to the "Valid Anagram" problem, but with a neat twist.

Since anagrams contain the same characters, we can assign each letter a unique prime number (from 2 up to the 26th prime, 103).  
The product of these primes for each word will be unique to that specific combination of characters — meaning all anagrams share the same product.

We’ll use a dictionary where:
    - Key  → the product of primes (unique signature for each anagram group)
    - Value → list of words (anagrams sharing the same product)

Finally, we’ll return the list of all the grouped values.
"""
class Solution(object):
    def groupAnagram(self, strs: list[str]) -> list[list[str]]:
        if strs is None or len(strs)==0:
            return None
        
        Prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 97, 101, 103]

        anaMap : dict[int, list[str]] = {}

        for s in strs:
            prod = 1
            for c in s:
                prod *= Prime[ord(c) - ord("a")]

            if prod in anaMap:
                anaMap[prod].append(s)
            else:
                anaMap[prod] = [s]
                
        return list(anaMap.values())
    
user_input = input("Enter list of string seperated by space: ").strip()
strs = list(user_input.split(" "))

solution = Solution()

print(solution.groupAnagram(strs))