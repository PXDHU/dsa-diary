"""
While playing an RPG game, you were assigned to complete
one of the hardest quests in the game.
There are n monsters you'll defeat in this quest.
Each monster i is described with two integer numbers - poweri and bonusi
To defeat the monster, you'll need atleast poweri experience
points. If you try fighting this monster without having enough points,
you'll lose immediately.
You will also gain bonusi experience points if you defeat this monster.
You can defeat monsters in any order. The quest turned out to be very
hard - you try to defeat the monsters but keep losing repeatedly.
Your friend told you that this quest is impossible to complete.
Knowing that, you're interested, what is the maximum possible number of monsters
you can defeat ?

Ip: the first line contains an integer n, denoting the number of monsters
The next line contains an integer, e, denoting your initial experience.
Each line i of the n subsequent lines(where 0<=i<n) contains an integer, poweri
which represents power of the corresponding monster.
Each line i of the n subsequent lines (where 0<= i< n) contains an integer
bonusi which represents bonus for the corresponding monster.
input:
2 -> n no of monster
123 -> initial experience points
78 -> monster 1 =poweri
130 -> monster 2 =poweri
10 -> monster 1 =bonusi
0 -> monster 2 =bonusi
output:
2
"""
class Solution:
    def RPGgame(self, exp, power, bonus):
        game = sorted(zip(power, bonus))
        ans = 0

        for p, b in game:
            if p > exp:
                break
            exp += b
            ans += 1
        
        return ans
    
solution = Solution()
n = int(input("Enter number of monsters: "))
exp = int(input("Enter experience level: "))
power = [int(input("Enter monster power: ")) for _ in range(n)]
bonus = [int(input("Enter kill bonus: ")) for _ in range(n)]


result = solution.RPGgame(exp, power, bonus)
print(result)