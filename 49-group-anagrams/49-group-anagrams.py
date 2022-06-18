class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        for string in strs:
            normalized = "".join(sorted(list(string)))
            groups[normalized].append(string)
            
        return groups.values()