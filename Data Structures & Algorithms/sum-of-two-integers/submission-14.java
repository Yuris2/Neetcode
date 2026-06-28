class Solution {
    public int getSum(int a, int b) {

        //4 = 100
        //2 = 010
        //
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
        
    }
}
