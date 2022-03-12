class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        ["abc","bcd","acef","xyz","az","ba","a","z"]
        
        
        az -> az
        ba -> aa
        cb -> 
        
        d = 25
        a -> 0 + 25 % 26 -> 25 -> z
        z -> 122 + 25 % 26 -> 17 -> 
             147
        d = 25
        b -> 1 + 25 % 26 -> 0 -> a
        a -> 0 + 25 % 26 -> 25 -> z
        find the shift value -> "z" - string[0]
        shift every char in the string by the value
        add key to the hashmap
        """
        
        groups = defaultdict(list)
        
        for string in strings:
            key = ""
            diff = ord("z") - ord(string[0])
            for char in string:
                shifted = (ord(char) + diff) % 26
                key += chr(ord("a") + shifted)
            groups[key].append(string)  
        return groups.values()
        
        
        
        