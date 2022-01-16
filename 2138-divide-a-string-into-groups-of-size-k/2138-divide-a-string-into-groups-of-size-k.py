class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
        Q1 from Weekly contest 276
        Submission time: 0:10:00
        Time spent: 10 mins
         
        Time Complexity: O(N*K)
        """
        groups = []
        
        string = ""
        for char in s:
            string += char
            if len(string) == k:
                groups.append(string)
                string = ""
        # check if last string needs to be filled in
        if string:
            string += fill*k
            groups.append(string[:k])
            
        return groups