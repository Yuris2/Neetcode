class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2
        totalLength = len(a) + len(b)
        halfLength = totalLength // 2

        if len(a) > len(b):
            a,b = b,a 
        
        l,r = 0, len(a) - 1

        while True:
            i = (l + r) // 2
            j = halfLength - i - 2

            Aleft = a[i] if i >= 0 else -2e9
            Aright = a[i + 1] if i < len(a) - 1 else 2e9
            Bleft = b[j] if j >= 0 else -2e9
            Bright = b[j + 1] if j < len(b) - 1 else 2e9

            if Aleft <= Bright and Bleft <= Aright:
                if totalLength % 2 == 0:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
                return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
        return None
        