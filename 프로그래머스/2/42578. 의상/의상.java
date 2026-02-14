import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, ArrayList<String>> map = new HashMap<>();
        
        for (String[] c: clothes) {
            String name = c[0];
            String category = c[1];
            
            if (map.containsKey(category))
                map.get(category).add(name);
            else {
                ArrayList<String> tmp = new ArrayList<>();
                tmp.add(name);
                map.put(category, tmp);
            }
        }
        
        for (String c: map.keySet()) {
            int count = map.get(c).size();
            answer *= count + 1;
        }
        return answer-1;
    }
}