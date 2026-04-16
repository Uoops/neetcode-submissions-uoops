from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            group[key].append(word)
        
        return [v for k, v in group.items()]