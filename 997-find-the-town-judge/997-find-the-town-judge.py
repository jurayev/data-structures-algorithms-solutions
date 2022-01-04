class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        Approach:
            1.descrease trust for person1 and increase trust for person2
            2.if there is a judge, trust count must be equals to n-1(everyone except judge)
            
        Time complexity O(N)
        Space complexity O(N)
        """
        trust_count = collections.Counter()
        
        for person1, person2 in trust:
            trust_count[person2] += 1
            trust_count[person1] -= 1
        
        for judge, count in trust_count.items():
            if count == n-1:
                return judge
        return n if n == 1 else -1