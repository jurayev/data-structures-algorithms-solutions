class Solution:
    class Solution:
        def maxProduct(self, nums: List[int]) -> int:
            """
            Time complexity  O(n)
            Space complexity O(1)

            Approach: Keep track of two products: max so far, min so far.
                      One every new calculation keep the best over all possible products

            Examples:
            [2,3,-2,4]
        max  2,6,-2,4
        min  2,6,-12,-12


            maxsofar = max(maxsofar * num, minsofar*num, num)
            minsofar = min(minsofar * num, max_sofar*num, num)


            [0,-1,-2, 4, 3, -2, 0,4,-2]

    max      0,0,  2, 8, 24, 48,0,4,0
    min      0,-1,-2,-8,-24,-48,0,0,-8


            [0,-48,48,-24,-6,-2,0,-8,-2]
            """
            best = float(-inf)
            max_so_far = 1
            min_so_far = 1

            for num in nums:
                new_max_so_far = max(max_so_far * num, min_so_far * num, num)
                new_min_so_far = min(max_so_far * num, min_so_far * num, num)
                max_so_far = new_max_so_far
                min_so_far = new_min_so_far
                best = max(best, min_so_far, max_so_far)
            return best

    def maxProductSecondSolution(self, nums: List[int]) -> int:
        """
        [0,-1,-2,4,3,-2,0,4,-2] => even => odds
                 ^
        [0,-1,-2,4,12,-2,0,4,-2]   no zeros, only pluses
        [0,-1,2,8,24,-48,0,-8,-2] no zeros, only minuses left -> right

        [0,-48,48,-24,-6,-2,0,-8,-2] no zeros, only minuses left <- right

        keep track of the max, including zero if any

        1. zero found    -> skip zeros
        2. minus found   -> skip minus
        3. minus found   -> include minus


        """
        best = current = nums[0]
        # first go -> no zeros, only pluses product

        n = len(nums)
        for i in range(1, n):
            num = nums[i]
            if num > 0 and current:
                current = max(current, current * num, num)
            else:
                current = num
            best = max(best, current)

        # second go -> no zeros, only minuses product, left -> right
        current = nums[0]
        best = max(best, current)

        for i in range(1, n):
            num = nums[i]
            if num and current:
                current *= num
            else:
                current = num
            best = max(best, current)
        # third go -> no zeros, only minuses product, left <- right
        current = nums[-1]
        best = max(best, current)
        for i in range(n - 2, -1, -1):
            num = nums[i]
            if num and current:
                current *= num
            else:
                current = num
            best = max(best, current)
        return best