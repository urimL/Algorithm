import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> result = new ArrayList<>();
        
        int n = progresses.length;
        int curDay = 0; int count = 0;
        
        for (int i=0;i<n;i++) {
            int remain = 100 - progresses[i];
            int day = (remain + speeds[i] - 1) / speeds[i];
            
            if (count == 0) {
                curDay = day;
                count = 1;
            } else if (day <= curDay) {
                count ++;
            } else {
                result.add(count);
                curDay = day;
                count = 1;
            }
        }
        
        if (count > 0) result.add(count);
        
        int[] answer = new int[result.size()];
        for (int i=0;i<result.size();i++) answer[i] = result.get(i);
        
        return answer;
    }
}