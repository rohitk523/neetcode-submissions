class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True 
        # return False
        from collections import Counter
        dict1= Counter(nums)
        for i in nums:
            if dict1[i]>1:
                return True
        else:
            return False
        