import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int count = 0;
        
        Deque<Character> q = new ArrayDeque<>();
        for (int i=0;i<s.length();i++)
            q.push(s.charAt(i));

        char now = q.pop();
        if (now=='(') return false;
        else count++;
        
        while (!q.isEmpty()) {
            if (q.peek()=='(') {
                if (count > 0) {
                    count--;
                } else return false;
            } else count++;
            
            q.pop();
        }
        
        if (count != 0) return false;
        return answer;
    }
}