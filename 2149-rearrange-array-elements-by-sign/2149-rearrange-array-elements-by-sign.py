class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        plus = [num for num in nums if num > 0]
        minus = [num for num in nums if num < 0]
        
        p_idx, m_idx = 0, 0
        
        while p_idx < len(plus):
            nums[p_idx+m_idx] = plus[p_idx]
            p_idx += 1
            nums[p_idx+m_idx] = minus[m_idx]
            m_idx += 1
        return nums
        