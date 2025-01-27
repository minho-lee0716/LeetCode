class Solution {
    public boolean isAnagram(String s, String t) {
        // 문자열 길이가 다르면 애너그램이 될 수 없음
        if (s.length() != t.length()) {
            return false;
        }

        while (s.length() > 0) {
            char curr = s.charAt(0); // 첫 번째 문자 가져오기
            long countS = s.chars().filter(c -> c == curr).count(); // s에서 문자 개수 세기
            long countT = t.chars().filter(c -> c == curr).count(); // t에서 문자 개수 세기

            if (countS != countT) {
                return false; // 개수가 다르면 애너그램 아님
            }

            // 해당 문자 제거
            s = s.replace(Character.toString(curr), "");
            t = t.replace(Character.toString(curr), "");

            // 문자열 길이 다시 확인
            if (s.length() != t.length()) {
                return false;
            }
        }

        return true;
    }
}