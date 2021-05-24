class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        list_ret = list()
        for i in range(0,l):
            # print('i=',i)
            for j in range(1,l):
                # print('j=',j)
                if nums[i] + nums[j] == target and i!=j:
                    # print(i,j)
                    return i,j
        return list_ret
        
s = Solution()
k = s.twoSum([2,5,5,11],10)
print(k)