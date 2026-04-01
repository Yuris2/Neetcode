class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        if len(A) > len(B):
            A,B = B,A
        
        l = 0
        r = len(A) - 1
        totalLength = len(A) + len(B)
        halfLength = totalLength // 2

        while True:
            i = (l + r) // 2
            j = halfLength - i - 2

            Aleft = A[i] if i >= 0 else -2e9
            Aright = A[i + 1] if i < len(A) - 1 else 2e9
            Bleft = B[j] if j >= 0 else -2e9
            Bright = B[j + 1] if j < len(B) - 1 else 2e9
            #[1,2,3,4]
            if Aleft <= Bright and Bleft <= Bright:
                if totalLength % 2 == 1:
                    return min(Aright, Bright)
                return (min(Aright,Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
        return None
            
        