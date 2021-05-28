
To Find actual missing value in between the min and max in list:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_return = []
        nums.sort(reverse=True)
        max_len = nums[0]
        index = 1
        while index <= max_len:
            if index not in nums:
                list_return.append(index)
            index+=1
        return list_return
    
s = Solution()
k = s.findDisappearedNumbers([1,1])
print(k)


Actual Submission:

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_return = []
        for i in range(0,len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        for i in range(0,len(nums)):
            if nums[i]>0:
                list_return.append(i+1)
        return list_return
    
s = Solution()
k = s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(k)