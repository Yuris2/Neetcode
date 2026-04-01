#[1,3]
#[2,4,5]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2

        if len(a) > len(b):
            a,b = b,a
        
        l,r = 0, len(a) - 1

        totalLength = len(a) + len(b)
        halfLength = totalLength // 2
        while True:
            #midpoint of smaller array
            i = (l + r) // 2
            j = halfLength - i - 2

            aLeft = a[i] if i >= 0 else -2e9
            aRight = a[i + 1] if i < len(a) - 1 else 2e9
            bLeft = b[j] if j >= 0 else -2e9
            bRight = b[j + 1] if j < len(b) - 1 else 2e9

            if aLeft <= bRight and bLeft <= aRight:
                if totalLength % 2 == 1:
                    return min(aRight, bRight)
                return (min(aRight, bRight) + max(aLeft, bLeft)) / 2.0
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1 
        
        return None

        