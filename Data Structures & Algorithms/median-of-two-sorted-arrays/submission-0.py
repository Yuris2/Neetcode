class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Goal is to partition based off the left side and the right side
        #Every element in left side is going to be greater than the right side
        #We can start by creating partition on smaller Array

        A,B = nums1, nums2
        #Making A the smaller element
        if len(A) > len(B):
            A,B = B,A
        
        totalLength = len(A) + len(B)
        half = totalLength // 2

        #[1,1,1]
        #[1,2,3]
        l, r = 0, len(A) - 1
        #Creating our partitions dynamically
        while True:
            #left partition of A index
            midA = (l + r) // 2
            #left partition of B index
            midB = half - midA - 2

            #If empty, assign to infinity
            Aleft = A[midA] if midA >= 0 else -2e9
            Aright = A[midA + 1] if (midA + 1) < len(A) else 2e9
            Bleft = B[midB] if midB >= 0 else -2e9
            Bright = B[midB + 1] if (midB + 1) < len(B) else 2e9

            #Condition checking
            if Aleft <= Bright and Bleft <= Aright:
                #Odd length
                if totalLength % 2 != 0:
                    return min(Aright, Bright)
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2
            #Too many elements in the A left
            elif Aleft > Bright:
                r = midA - 1
            else:
                l = midA + 1
        






        
        