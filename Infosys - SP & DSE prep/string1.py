"""
Given a string "Number" representing a positive integer and a character "Digit".
Return resulting string after removing exactly one occurence of digit
such that the value of the resulting string in decimal form is maximum.

I/P: number = "1321", digit = "1"
O/P: "321"

"""
class Solution:
    def removeMax(self, number, digit):
        ans = []

        for i in range(len(number)):
            if number[i]==digit:
                t = number[:i] + number[i+1:]
                ans.append(t)
            
        return int(max(ans))

number = str(input("Enter the number: "))
digit = str(input("Enter the digit: "))

solution = Solution()

result = solution.removeMax(number, digit)

print(result)
