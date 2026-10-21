class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seenMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int needed = target - nums[i];
            if (seenMap.containsKey(needed)) {
                return new int[]{seenMap.get(needed), i};
            }
            seenMap.put(nums[i], i);
        }
        return new int[0];
    }
}
