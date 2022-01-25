class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        
        top_idx = 1
        
        while top_idx < len(arr) and arr[top_idx-1] < arr[top_idx]:
            top_idx += 1
        
        top_idx -= 1
        if top_idx == 0 or top_idx == len(arr)-1:
            return False
        
        while top_idx+1 < len(arr) and arr[top_idx] > arr[top_idx+1]:
            top_idx += 1
            
        return top_idx == len(arr)-1