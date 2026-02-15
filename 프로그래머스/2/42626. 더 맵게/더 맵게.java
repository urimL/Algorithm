import java.util.*;

class Solution {
    public int solution(int[] scoville, int k) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int c: scoville) 
            pq.offer(c);
        
        while (!pq.isEmpty()) {
            int first = pq.poll();
            if (first >= k) return answer;
            
            if (pq.isEmpty()) return -1;
            
            int second = pq.poll();
            int tmp = first + second * 2;
            answer++;
            pq.offer(tmp);
        }
        
        return answer;
    }
}