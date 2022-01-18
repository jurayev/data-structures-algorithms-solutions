class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return result
        
        q = deque([[nums[0]]])
        while q:
            curr_arr = q.popleft()
            n = len(curr_arr)
            if n == len(nums):
                result.append(curr_arr)
                continue

            for i in range(n+1):
                next_arr = curr_arr[:]
                next_arr.insert(i, nums[n])
                q.append(next_arr)

        return result
        
        
    def permuteSwaps(self, nums: List[int]) -> List[List[int]]:   
        result = []
        self.find(nums.copy(), 0, result)
        return result

    def find(self, nums, start, result):
        if start >= len(nums):
            result.append(nums.copy())
            return

        for end in range(start, len(nums)):
            self.swap(start, end, nums)
            self.find(nums, start+1, result)
            self.swap(start, end, nums)

    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]