class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        for string in strs:
            alphabet = [0] * 26
            
            for char in string:
                idx = ord(char) - ord("a")
                alphabet[idx] += 1
            hash_key = "#".join(map(str, alphabet))
            groups[hash_key].append(string)
            
        return groups.values()
        
    
    
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        for string in strs:
            normalized = "".join(sorted(list(string)))
            groups[normalized].append(string)
            
        return groups.values()