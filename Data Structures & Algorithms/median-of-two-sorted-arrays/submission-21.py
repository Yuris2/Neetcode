class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2

        if len(a) > len(b):
            a,b = b,a 
        
        totalLength = len(a) + len(b)
        halfLength = totalLength // 2

        l,r = 0, len(a) - 1

        while True:
            i = (l + r) // 2
            j = halfLength - i - 2

            aLeft = a[i] if i >= 0 else -2e9
            aRight = a[i + 1] if i < len(a) - 1 else 2e9
            bLeft = b[j] if j >= 0 else -2e9
            bRight = b[j + 1] if j < len(b) - 1 else 2e9

            if aLeft <= bRight and bLeft <= aRight:
                if totalLength % 2 == 0:
                    return (min(bRight, aRight) + max(bLeft, aLeft)) / 2.0
                return min(bRight, aRight)
            elif aLeft > bRight:
                r = i - 1
            else:
                l = i + 1
        
        return
            