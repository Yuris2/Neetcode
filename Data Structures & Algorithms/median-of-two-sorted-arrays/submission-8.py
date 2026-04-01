class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        if len(A) > len(B):
            A,B = B,A
        
        totalLength = len(A) + len(B)
        #Partition length
        halfLength = totalLength // 2 

        l,r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = halfLength - i - 2

            Aleft = A[i] if i >= 0 else -2e9
            Aright = A[i + 1] if i < len(A) - 1 else 2e9
            Bleft = B[j] if j >= 0 else -2e9
            Bright = B[j + 1] if j < len(B) - 1 else 2e9

            if Aleft <= Bright and Bleft <= Aright:
                if totalLength % 2 != 0:
                    return min(Aright, Bright)
                return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
        return -1
            
        