class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        side_length = total // 4
        sides = [0] * 4

        return self.dfs(0, side_length, sides, matchsticks)
    
    def dfs(self, index, length, sides, matchsticks):
        if sides[0] == sides[1] == sides[2] == sides[3] == length:
            return True
        
        for i in range(4):
            if sides[i] + matchsticks[index] > length:
                continue
            
            if i > 0 and sides[i - 1] == sides[i]:
                continue
                
            sides[i] += matchsticks[index]
            if self.dfs(index + 1, length, sides, matchsticks):
                return True
            sides[i] -= matchsticks[index]
        
        return False