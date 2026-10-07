class Solution {
    public int removeElement(int[] nums, int val) {
        // remove all occurrences of val in nums
        // can change order
        // return num elements in nums not equal to val

        // one pointer to keep track of where the next valid element should be place, one pointer to go thought each element in nums
        // if a num is not the val, swap it with the next valid location
        
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                 nums[k] = nums[i];
                 k++;
            }
        }
        return k;
    }
}