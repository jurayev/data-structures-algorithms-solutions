class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]   target = 0
          ^
            ^
       result [-1,-1,2] [-1,0,1]


        TC O(n^2), using set for seen values and set for keeping all duplicate hashes
        SC O(2N)
        """
        triplets = []
        n = len(nums)
        duplicates = set()
        seen = {}
        for i in range(n):
            if nums[i] not in duplicates:
                duplicates.add(nums[i])

                for j in range(i + 1, n):
                    value = 0 - nums[i] - nums[j]
                    # hash_val = map(str, sorted([nums[i], value, nums[j]]))
                    # hash_val = "".join(hash_val)
                    if value in seen and seen[value] == i:
                        triplets.append([nums[i], value, nums[j]])
                    # duplicates.add(hash_val)
                    seen[value] = i

        return triplets

    def threeSumSortHashMap(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]   target = 0
          ^
            ^
        [-4,-1,-1,0,1,2]   -> result [-1,-1,2] [-1,0,1]
             ^
                    ^

        TC O(n^2), sorted, using hasmap
        SC O(n), TimSort in python uses constant space
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        triplets = []
        for i in range(0, n):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            target = -sorted_nums[i]
            # solve two sum
            seen = set()
            j = i + 1
            while j < n:
                value = target - sorted_nums[j]
                if value in seen:
                    triplets.append([sorted_nums[i], value, sorted_nums[j]])
                    while j < n - 1 and sorted_nums[j] == sorted_nums[j + 1]:
                        j += 1
                seen.add(sorted_nums[j])
                j += 1

        return triplets

    def threeSumSortThreePointers(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]   target = 0

        [-4,-1,-1,0,1,2]   -> result [-1,-1,2] [-1,0,1]
          ^
            ^
               ^

        TC O(n^2),sorted, 3 pointers, solve subproblems using twoSum approach
        SC O(1), TimSort in python uses constant space
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        triplets = []
        for i in range(0, n - 2):
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i]: continue
            # solve two sum
            j = i + 1
            k = n - 1
            while j < k:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

                if total == 0:
                    triplets.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                if total < 0:
                    while j + 1 < k and sorted_nums[j] == sorted_nums[j + 1]:
                        j += 1
                    j += 1
                else:
                    while j < k - 1 and sorted_nums[k] == sorted_nums[k - 1]:
                        k -= 1
                    k -= 1

        return triplets

    def threeSumAdditionalSpaceForSet(self, nums: List[int]) -> List[List[int]]:
        """
        TC O(n^2) sorted, 3 pointers, set for duplicates stored like hash value -> "-101"
        SC O(n^2) to store hash values in the set
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        triplets = []
        seen = set()
        for i in range(0, n - 2):
            # solve two sum
            j = i + 1
            k = n - 1
            while j < k:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                hash_value = str(sorted_nums[i]) + str(sorted_nums[j]) + str(sorted_nums[k])
                if total == 0 and hash_value not in seen:
                    triplets.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    seen.add(hash_value)
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return triplets