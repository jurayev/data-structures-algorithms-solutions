class Solution:
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """               0 1 2 3
        [4,1,2], nums2 = [1,0,3,4,2]
        
        1. Approach: Monotonic decreasing stack
            1. start backwards in nums2
            2. add every el to stack 
            3. when last el in stack is smaller -> pop it from stack
            4. after appending the current el, we instantly know that i-1 element is next greater
        2.Examples:
            num = 1
            stack = [4, 3, 1]
            search_nums {4:0, 1:1, 2:2}
             0 1
            [2,4]  [1,2,3,4]

            [4,3,2,1]
            
        3. Time Complexity O(n+m)
            Space Complexity O(n+m)
        """
        search_nums = {num: idx for idx, num in enumerate(nums1)}
        next_els = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            num = nums2[i]
            while stack and stack[-1] <= num:
                stack.pop()
            
            if num in search_nums:
                idx = search_nums[num]
                next_els[idx] = stack[-1] if stack else -1
            stack.append(num)
        return next_els
    

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """               0 1 2 3
        [4,1,2], nums2 = [1,0,3,4,2]
        
        1. Approach:
            1.add all elements from nums2 in reverse order to stack keeping track of the next greater element
            2. for every num in nums2 store the position in hashmap for quick access
            3. iterate over nums1 and get the next greater element from hashmap
        [(2,-1), (4,-1), (3,4), (0,3), (1,3)]
        """
        n = len(nums1)
        m = len(nums2)
        next_els = [-1] * n 
        indexes = {num: idx for idx, num in enumerate(nums2)}
        
        for idx, num in enumerate(nums1):
            start_idx = indexes[num] + 1
            for i in range(start_idx, m):
                if nums2[i] > num:
                    next_els[idx] = nums2[i]
                    break
        return next_els