class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        
        
        "[[Hello]][World]"
        """
        temp = []
        for string in strs:
            temp.append(string.replace("#", "##"))
        return " # ".join(temp)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = s.split(" # ")
        for idx, string in enumerate(strs):
            strs[idx] = string.replace("##", "#")
        return strs
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))