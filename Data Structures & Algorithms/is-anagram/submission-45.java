class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (char c : s.toCharArray()) {
            if (!sMap.containsKey(c)) {
                sMap.put(c, 1);
            } else {
                sMap.put(c, sMap.get(c) + 1);
            }
        }
        for (char c : t.toCharArray()) {
            if (!tMap.containsKey(c)) {
                tMap.put(c, 1);
            } else {
                tMap.put(c, tMap.get(c) + 1);
            }
        }

        return sMap.equals(tMap);
        
    }
}
