class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        i,j,k=0,1,2
        count = 0
        while i < len(nums) and  j < len(nums) and  k <len(nums) :
            if nums[i] == nums[j]:
                j+=1
                continue
            if nums[j] == nums[k]:
                k+=1
                continue
            d1 = nums[j] - nums[i]
            d2= nums[k]-nums[j]

            if d1<diff:
                j+=1
            elif d1>diff:
                i+=1
            elif d2<diff:
                k+=1
            elif d2>diff:
                j+=1
            else:
                count+=1
                i+=1
                j+=1
                k+=1
        return count                        
