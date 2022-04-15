class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Ex 1:
        [4,5,6,7,0,1,2] t=0
        Ex 2:
        [4,5,6,7,0,1,2], target = 3
        1. Idea: just traverse all numbers and return index if target is found
                else -1
                Time O(N)
                Space O(1)
        2. Idea: using bin search.
            1. Identify if range is still rotated, check leftmost and mid
                leftmost > mid -> rotated
                    check target between mid and right
                        go right
                        go left
                not rotated
                    check target between left and mid
                        go left
                        go right
            2. if rotated, check target if greater or equal than leftmost number 
                    -> go left
                    -> go right
            3. not rotated, 
            4. Handle corner cases
            5. if leftpointer > right_pointer: return -1
            
        Ex 1:
                     m
        [5,6,0,1,2,3,4] t=0, t=5, t=4
                     l            
                     r
        Ex 2:
                 m
        [4,5,6,7,8,1,2], t=8, t=9
                   l
                 r
        """
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            # check if left part is rotated
            if nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    # go right
                    left = mid + 1
                else:
                    right = mid - 1
            else: #not rotated
                if nums[left] <= target < nums[mid]:
                    # go left
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return -1
                
        
        