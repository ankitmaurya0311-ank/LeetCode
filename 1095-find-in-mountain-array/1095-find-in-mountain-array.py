# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l= 0
        r = mountainArr.length()-1
        while l<r:
            mid = l+(r-l)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid +1 
            else :
                r = mid    
        peak = l
        l=0
        r = peak 
        while l<=r:
            mid = l+ (r-l)//2
            value = mountainArr.get(mid)
            if value == target :
                return mid 
            if value < target :
                l = mid +1
            else : 
                r = mid -1
        l = peak +1
        r = mountainArr.length()-1
        while l<=r:
            mid = l+ (r-l)//2
            value = mountainArr.get(mid)
            if value == target :
                return mid 
            if value > target :
                l = mid +1
            else : 
                r = mid -1
        return -1



        