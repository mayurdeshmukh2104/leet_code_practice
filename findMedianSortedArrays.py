class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        if len(nums1) == 1 and nums1[0] == 0:
            nums1[0] = ''
            nums3 = nums2
        elif len(nums2) == 1 and nums2[0] == 0:
            nums2[0] = ''
            nums3 = nums1
        elif len(nums1) == 0:
            nums3 = nums2
        elif len(nums2) == 0:
            nums3 = nums1
        else:
            nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        # print(nums3)
        l_of_list = len(nums3)
        if l_of_list % 2 == 0:
            a1 = l_of_list//2
            a2 = a1
            if a2-1 == -1:
                return 0
            # print((nums3[a1]+(nums3[a2-1]))/2)
            return (nums3[a1]+(nums3[a2-1]))/2
        else:
            mid = int(l_of_list/2 - 0.5)
            return nums3[mid]