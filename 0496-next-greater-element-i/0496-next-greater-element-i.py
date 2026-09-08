class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                small = stack.pop()
                next_greater[small] = num
            stack.append(num)
        return [ next_greater.get(num,-1) for num in nums1]        