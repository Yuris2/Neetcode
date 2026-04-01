class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Try to use binary search to try and construct a continguous array
        #Partition Condition
            #[1,2,5,8,9]
            #[1,5]
            # 
            #[2,8,9]
            # l  r

            #i = 1          j = 2
        a,b = nums1, nums2
        
        if len(a) > len(b):
            a,b = b,a
        
        totalLength = len(a) + len(b)
        halfLength = totalLength // 2

        l,r = 0, len(a) - 1

        while True:
            i = (l + r) // 2
            j = halfLength - i - 2

            Aleft = a[i] if i >= 0 else -2e9
            Aright = a[i + 1] if  i < len(a) - 1 else 2e9
            Bleft = b[j] if j >= 0 else -2e9
            Bright = b[j + 1] if  j < len(b) - 1 else 2e9

            if Aleft <= Bright and Bleft <= Aright:
                if (totalLength) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            




        
        