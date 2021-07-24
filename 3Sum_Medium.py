class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l,r = i+1, len(nums) - 1
            while l<r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l +=1
                else:
                    result.append([a,nums[l],nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return result
        
s = Solution()
li = [-1,0,1,2,-1,-4]
ans = s.threeSum(li)
print(ans)
