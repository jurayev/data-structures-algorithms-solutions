class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
