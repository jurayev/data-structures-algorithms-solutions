class Solution:
    def wordCount(self, startw: List[str], targetw: List[str]) -> int:
        """
        Approach:
            Sort anagram words
            Try every possible word in targets by removing one letter
            If target word exist in starting words, increment counter
        Examples:
            ["tack","act","acti"]
            ["ab","a"]
            ["abc","abcd"]
            ["ab","ac"]
            ["ab","abcd"]
            ["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"]
            ["r","am","jg","umhjo","fov","lujy","b","uz","y"]
        
        Complexity:
            Time O(NlogN + M*K^2)
            Space O(NlogN + S + T)
        """
        s_words = set()
        for idx, word in enumerate(startw):
            s_words.add("".join(sorted(word)))
        t_words = []    
        for idx, word in enumerate(targetw):
            t_words.append("".join(sorted(word)))
            

        string_count = 0
        for word in t_words:
            for i in range(len(word)):
                match_word = word[:i] + word[i+1:]
                if match_word in s_words:
                    string_count += 1
                    break
        return string_count