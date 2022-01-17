class Solution:
    def subsetsWithDup(self, num: List[int]) -> List[List[int]]:
        subsets = [[]]
        start_indexes = defaultdict(int)
        nums = sorted(num)
        for num in nums:
            new_subsets = []
            end_i = len(subsets)
            for i in range(start_indexes[num], end_i):
                new_subsets.append(subsets[i] + [num])
            subsets.extend(new_subsets)
            start_indexes[num] = end_i
        return subsets

    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        duplicates = set()
        subsets = [ [] ]
        nums = sorted(nums)
        for i in range(len(nums)):
            generated = []
            for subset in subsets:
                new_set = subset[:] + [nums[i]]
                hash_key = "".join(map(str,new_set))
                if hash_key in duplicates:
                    continue

                duplicates.add(hash_key)
                generated.append(subset[:] + [nums[i]])
            subsets.extend(generated)
        return subsets
    
        subsets = [[]]
