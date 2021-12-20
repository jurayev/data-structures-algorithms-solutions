class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        
        sorted_arr = sorted(arr)
        min_diff = float(inf)
        pairs = []
        
        n = len(arr)
        for i in range(n-1):
            min_diff = min(min_diff, sorted_arr[i+1] - sorted_arr[i])
            
        for i in range(n-1):
            num1 = sorted_arr[i]
            num2 = sorted_arr[i+1]
            if num2 - num1 == min_diff:
                pairs.append([num1, num2])
                
        return pairs
            