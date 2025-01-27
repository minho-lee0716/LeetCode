class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        while (s.length() > 0) {
            char curr = s.charAt(0);
            long countS = s.chars().filter(c -> c == curr).count();
            long countT = t.chars().filter(c -> c == curr).count();

            if (countS != countT) {
                return false;
            }

            s = s.replace(Character.toString(curr), "");
            t = t.replace(Character.toString(curr), "");

            if (s.length() != t.length()) {
                return false;
            }
        }

        return true;
    }
}