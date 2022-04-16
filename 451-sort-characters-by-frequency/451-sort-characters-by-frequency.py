class Solution:
    def frequencySort(self, s: str) -> str:
        """
        tarerer
        
        counts = {
        e: 2
        t: 1
        r: 3
        a: 1
        }
        
        out = rrreeat
        
        Idea 1:
            count all chars
            sort counts in decreasing order
            join the letter one by one, with respect to the counts
            
            Time O(N log N) [O(26 log 26)], N is the number of unique chars
            Space O(N)
        Idea 2:
            count all chars
            sort counts in decreasing order using bucket sort(linear sorting) 
            Allocate buckets from 0 till z
            join the letter one by one, with respect to the counts
            
            Time O(N), N is the number of total chars
            Space O(N), to store in hashmap
        """
        
        counts = Counter(s)
        max_count = max(counts.values())
        buckets = [[] for _ in range(max_count+1)]
        for letter, count in counts.items():
            buckets[count].append(letter)
        
        sorted_string = []
        for bucket in range(max_count, -1, -1):
            letters = buckets[bucket]
            if not letters: continue
            for letter in letters:
                same_letter_string = letter * bucket
                sorted_string.append(same_letter_string)
        
        return "".join(sorted_string)
            