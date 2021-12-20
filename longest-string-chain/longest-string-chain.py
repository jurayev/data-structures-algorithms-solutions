class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        a: 1
        b: 1
        ba: 2
        bca: 3
        bda: 3
        ["a","b","ba","bca","bda","bdca"]
                                    ^
          
        
        
        """
        search_words = sorted(words, key=len)
        seen_chains = {"": 0}
        
        longest_chain = 0
        for word in search_words:
            seen_chains[word] = seen_chains.get(word, 1)
            for i in range(len(word)):
                candidate = word[:i] + word[i+1:]
                if candidate in seen_chains:
                    seen_chains[word] = max(seen_chains[word], seen_chains[candidate]+1)
                
            longest_chain = max(longest_chain, seen_chains[word])

        return longest_chain
        
        
        