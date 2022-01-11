class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        From BiWeekly Contest 69, Q3
        Submission time - 1h 18m
        Examples:
            ["cc","ll","ll","ll","xx","xx","xx","xx","xx"] => 14

            [ll","ll","ll","xx","xx","xx","xx","xx"] => 14
            [ll","ll","xx","xx","xx","xx","xx"] => 14


            ["cc","ll","ll","ll","ty","yt", "ab", "ab", "xx","xx","xx","xx","xx"] => 18
            ["cc","ll","xx", "pp"]
              1     3    3    5
        
              xxllccllxx

              llxxxxxxll
        
            ["lc", ab","ty","yt","lc","cl","ab"]  => 6
        Approach:
            word counters:
                gg: 2
                kk: 5
                ty: 2
                yt: 1
            categorization:
                none-palindrome    - [ab] 
                palindrome pairs   - [ty, yt] [lc, cl]
                single palindromes - [gg, kk]

            best = pair len * min(p1, p2 counts)
            best = 2 * word count
        Complexities:
            Time O(M), where M is the len of all words
            Space O(N), where N is the len of all unique words 
        """
        freq = Counter(words)

        best = 0
        center = 0
        keys = list(freq.keys()) # save a copy of all keys

        for word1 in keys:
            word2 = "".join(word1[::-1])
            if word1 == word2:  # palindrome itself
                count = freq[word1]
                if count % 2 == 1:
                    count -= 1
                    center = 2
                best += 2 * count
                freq.pop(word1, -1) # mark as used by removing from freq set

            best += 4 * min(freq[word1], freq[word2])

            freq.pop(word1, -1) # mark as used by removing from freq set
            freq.pop(word2, -1) # mark as used by removing from freq set
        
        return best + center