class MinStack {
    private Stack<Integer> stack; // normal stack
    private Stack<Integer> minStack; // just for getMin(), keep track of minimum at each element

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    // stack = [1, 3, -1]
    // minStack = [1, 1, -1]
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() || val < minStack.peek()) { // new min
            minStack.push(val);
        } else { // keep current min
            minStack.push(minStack.peek());
        }
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
