class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ls = [[]]
        nums.sort()
        for i in nums:
            ls +=[ele + [i] for ele in ls if ele+[i] not in ls]
        return ls