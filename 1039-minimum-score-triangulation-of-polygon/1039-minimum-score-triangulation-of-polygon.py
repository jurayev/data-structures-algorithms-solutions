class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        @lru_cache(None)
        def get_min_score(i, j):
            min_score = float(inf)
            for k in range(i+1, j):
                score = values[i] * values[k] * values[j]
                min_score = min(min_score, get_min_score(i, k) + get_min_score(k, j) + score)
                
            return min_score if min_score < float(inf) else 0
        
        return get_min_score(0, n-1)