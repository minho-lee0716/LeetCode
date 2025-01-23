class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> mapping = Map.of('(', ')', '{', '}', '[', ']');

        for (char charInS : s.toCharArray()) {
            if (mapping.containsKey(charInS)) {
                stack.push(charInS);
            } else if (stack.isEmpty()) {
                return false;
            } else if (mapping.containsValue(charInS)) {
                if (charInS != mapping.get(stack.pop())) {
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }
}