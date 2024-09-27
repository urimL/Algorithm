import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        int pos = 0;
        
        Queue<Integer> q = new LinkedList<>();
        for (int p: prices) {
            q.add(p);
        }
        
        while (!q.isEmpty()) {
            int now = q.poll();
            int count = 0;            
            
            for (int i: q) {
                count++;
                if (i<now) break;
            }
            
            answer[pos] += count;
            pos++;
            
        }
        
        return answer;
    }
}