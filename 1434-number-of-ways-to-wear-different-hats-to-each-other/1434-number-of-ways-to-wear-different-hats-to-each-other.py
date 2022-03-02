class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        """
          x     x     x
        [[3,4],[4,5],[5,3]]
                      ^
                
             x x x
        [1,2,3,4,5,6]
        
        
        subproblems:
                try to iterate over all possible combinations taking only 1 hat from each 
                set, marking this hat label as used
                if we can reach the last array and find a free hat, count + 1
                else backtrack and try hats[i][j..n-1]
        recurrence:
                count_ways(person_idx):
                    for j .... n-1:
                        count += count_ways(j)
        base cases:
                if person_idx >= total persons:
                    return 1
        
        answer:
                count_ways(0)
        
        Complexities:
                Time O(N^2*M) -> n persons, m hats
                Space O(N^2)
                
        mask = 1000000000100010
              40...109876543210
              
        1: []
        2: []
        3: [0]
        4: [0,1]
        5: [1,2]
        """
        @lru_cache(None)
        def count_ways(hat_id, all_person_mask, person_mask):
            if all_person_mask == person_mask:
                return 1
            if hat_id > 40:
                return 0
            
            count = count_ways(hat_id+1, all_person_mask, person_mask)
            for person in hat_to_person[hat_id]:
                if person_mask & (1 << person) != 0:
                    continue
                count += count_ways(hat_id+1, all_person_mask, person_mask ^ (1 << person))
            return count 
        
        hat_to_person = defaultdict(list)
        for person_id, hat_ids in enumerate(hats):
            for hat_id in hat_ids:
                hat_to_person[hat_id].append(person_id)
        return count_ways(1, (1 << len(hats)) - 1, 0) % (10**9 + 7)