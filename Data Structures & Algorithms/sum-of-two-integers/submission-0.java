class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            //Calculate the carry
            int carry = (a & b) << 1;
            //XOR a and b
            a = a ^ b;
            //Set b to the carry
            b = carry;
        }
        return a;

    }
}
