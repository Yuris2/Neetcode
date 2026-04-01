class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #[1,2,3,3,4,4,5,7]
        #(3 + 4) // 2 = 3.5
        #[1,2,3,4,5]
        #[3,4,7]
        #R = 0
        #A left = 3, B left = 3
        #A right = 4, B right = 4

        #6 elements
        #Index 1 on element A
        A,B = nums1, nums2

        if len(B) < len(A):
            A,B = B,A
        
        totalLength = len(A) + len(B)
        halfLength = totalLength // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = halfLength - i - 2

            Aleft = A[i] if i >= 0 else -2e9
            Aright = A[i + 1] if (i + 1) < len(A) else 2e9
            Bleft = B[j] if j >= 0 else -2e9
            Bright = B[j + 1] if (j + 1) < len(B) else 2e9

            if Aleft <= Bright and Bleft <= Aright:
                if totalLength % 2 == 1:
                    return min(Bright, Aright)
                return (max(Bleft, Aleft) + min(Aright, Bright)) / 2
            elif Aleft >= Bright:
                r = i - 1
            else:
                l = i + 1
            



        

        

        
        