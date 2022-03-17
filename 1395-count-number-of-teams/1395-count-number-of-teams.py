class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        requirements:
        3 elements
        2 valid teams:
            1. i < j < k
            2. i > j < k
        can reuse the same elements
        
        Ideas:
        
        1. Brute Force.
        Fix i, j, move k....n-1
        Fix i, move j till k, fix k
        Move i till j, fix j and k
        if any valid team can be formed -> add to the result
        
        2. Optimize with DP
        do idea 1 with cache optimizations
        
        a. subproblems:
            take any 3 element
            try valid team 1 option
            try valid team 2 option
            return count
        b. recurrence:
            max_teams(i, j, soldiers, inc) = max_teams(i..j, j..n, soldiers, inc=true)
            
            [2,5,3,4,1]
             i j
        c: base cases:
            if soldiers == 3:
                count += 1
            if j >= len:
                return
        c: answer = max_teams(0,1,0,true) + max_teams(0,1,0,false)
        
        
        [2,5,3,4,1]
         i j
         c = 0
         s = 1
            ij
                s = 2
                c = 0
        i    j
        s = 1
        c = 0
             i j
                s = 2
                c = 0
                 i j
                    s = 3
                    c = 1
            i j
                s = 2
                c = 1
        """
        @lru_cache(None)
        def max_teams(i, soldiers, is_increasing):
            if soldiers >= 3:
                return 1
            
            count = 0
            for j in range(i+1, len(rating)):
                if is_increasing and rating[i] < rating[j]:
                    count += max_teams(j, soldiers+1, is_increasing)
                elif not is_increasing and rating[i] > rating[j]:
                    count += max_teams(j, soldiers+1, is_increasing)
  
            return count
        count = 0
        for i in range(0, len(rating)-2):
            count += max_teams(i, 1, True) + max_teams(i, 1, False)
        
        return count
        