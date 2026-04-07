class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {c:i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if not self.right_order(w1, w2, rank):
                return False
        
        return True

    def right_order(self, w1, w2, rank):
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                return rank[w1[i]] < rank[w2[i]]
        
        return len(w1) <= len(w2)