class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int res = students.length;
        int[] cnt = new int[2];
        for (int student : students) {
            cnt[student]++;
        }
        for (int sandwich : sandwiches) {
            if (cnt[sandwich] > 0) {
                cnt[sandwich]--;
                res--;
            }
            else {
                break;
            }
        }
        return res;
    }
}