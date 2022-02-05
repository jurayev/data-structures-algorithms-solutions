class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        """
        [2,-1,1,2,2]
              s
              f
        
        [-1,2]
          s
          f
            
        detect self loops
        detect if all pos or all neg
        
        Time O(N*M), N is the total start positions. M is the max loop steps
        Space O(1)
        """
        n = len(nums)
        for i in range(0, len(nums)):
            check = self.check_all_neg if nums[i] < 0 else self.check_all_pos
            fast = i
            slow = i

            while True:
                if not check(nums[fast]) or self.self_loop(nums, fast, n):
                    break
                fast = (fast + nums[fast]) % n
                
                if not check(nums[fast]) or self.self_loop(nums, fast, n):
                    break
                fast = (fast + nums[fast]) % n
                
                if not check(nums[slow]) or self.self_loop(nums, slow, n):
                    break
                slow = (slow + nums[slow]) % n
                if fast == slow:
                    return True
            
        return False
    
    def self_loop(self, nums, idx, n):
        next_idx = (idx + nums[idx]) % n
        return idx == next_idx
    
    def check_all_pos(self, step):
        return 0 <= step
    
    def check_all_neg(self, step):
        return 0 > step