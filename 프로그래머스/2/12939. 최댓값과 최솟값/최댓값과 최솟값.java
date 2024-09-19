import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] tmp = s.split(" ");
        int min, max, n;
        
        min = max = Integer.parseInt(tmp[0]);
        for (int i=1; i<tmp.length; i++) {
            n = Integer.parseInt(tmp[i]);
            if (min < n) min = n;
            if (max > n) max = n;
        }
        answer = max + " " + min;
        
        return answer;
    }
}