class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxOnes = 0;
        int ones = 0;
        for (int num : nums) {
            if (num == 1) {
                ones++;
                maxOnes = Math.max(ones, maxOnes);
            }
            else {
                ones = 0;
            }
        }
        return Math.max(ones, maxOnes);
    }
}