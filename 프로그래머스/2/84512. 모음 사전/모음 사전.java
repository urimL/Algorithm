import java.util.*;

class Solution {
    static char[] alphabet;
    static String finalWord;
    static int count;
    static boolean found;
    
    public int solution(String word) {
        found = false;
        finalWord = word;
        alphabet = new char[]{'A','E','I','O','U'};
        String now = "";
        
        backtrack(now);
        
        return count;
    }
    
    private static void backtrack(String now) {
        if (found) return;
        
        if (!now.isEmpty()) {
            count ++;
            if (now.equals(finalWord)) {
                found = true;
                return;
            }
        }

        if (now.length() == 5) return;
        
        for (char a : alphabet) { 
            backtrack(now + a);
        }
    }
}