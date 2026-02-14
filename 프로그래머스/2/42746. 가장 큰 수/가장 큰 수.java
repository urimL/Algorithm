import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        List<String> strnum = new ArrayList<>();
        for (int n: numbers)
            strnum.add(Integer.toString(n));
        strnum.sort((a, b) -> (b + a).compareTo(a + b));
        
        if (strnum.get(0).equals("0")) return "0";
        for (String s: strnum) {
            answer += s;
        }
        
        return answer;
    }
}