class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        totalLen = len(A) + len(B)
        halfLen = totalLen // 2

        if len(B) < len(A):
            A,B = B,A
        
        l,r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j =  halfLen - i - 2

            Aleft = A[i] if i >= 0 else -2e9
            Aright = A[i + 1] if (i + 1) < len(A) else 2e9
            Bleft = B[j] if j >= 0 else -2e9
            Bright = B[j + 1] if (j + 1) < len(B) else 2e9

            if Aleft <= Bright and Bleft <= Aright:
                if totalLen % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            

        
        