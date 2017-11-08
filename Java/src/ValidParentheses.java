import java.util.Stack;

/**
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 * <p>
 * Accepted.
 */
public class ValidParentheses {

    public boolean isValid(String s) {
        if (s == null || s.length() == 0 || s.length() == 1) {
            return false;
        }

        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && (c == ')' && stack.peek() == '('
                    || c == ']' && stack.peek() == '['
                    || c == '}' && stack.peek() == '{')) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }

//        System.out.println("======");
//        for (char c : stack) {
//            System.out.print(c + " ");
//        }
//        System.out.println("\n*****");

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        ValidParentheses vp = new ValidParentheses();
        // Expected: true
        System.out.println(vp.isValid("()"));
        // Expected: true
        System.out.println(vp.isValid("()[]{}"));
        // Expected: false
        System.out.println(vp.isValid("("));
        // Expected: false
        System.out.println(vp.isValid("(]"));
        // Expected: false
        System.out.println(vp.isValid("([)]"));
    }

}