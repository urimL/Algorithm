import java.util.*;
import java.io.*;

class Solution {
    public String solution(String[] participant, String[] completion) {  
        HashMap<String, Integer> map = new HashMap<>();
        String answer = "";
        
        for (String p: participant) {
            if (!map.containsKey(p)) 
                map.put(p,1);
            else
                map.replace(p,map.get(p)+1);
        }
        
        for (String c: completion) {
            if (map.containsKey(c)) {
                map.replace(c,map.get(c)-1);
            }
        }
        
        for (String key: map.keySet()) {
            if (map.get(key) > 0) {
                answer = key;
            }
        }
        
        return answer;
    }
}