class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        ["abc","bcd","acef","xyz","az","ba","a","z"]
        
        
        az -> bx
        """
        
        groups = defaultdict(list)
        
        for string in strings:
            key = ""
            diff = ord("z") - ord(string[0])
            for char in string:
                shifted = (ord(char) + diff) % 26
                key += chr(shifted)
            groups[key].append(string)
            
            
        return groups.values()
        
        
        
        