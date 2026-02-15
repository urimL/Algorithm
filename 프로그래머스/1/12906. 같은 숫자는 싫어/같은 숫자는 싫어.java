import java.util.*;

public class Solution {
    public int[] solution(int []arr) {

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i=arr.length-1;i>=0;i--) {
            int a = arr[i];
        
            if (deque.isEmpty()) deque.push(a);
            else {
                if (deque.peek() == a) continue;
                deque.push(a);
            }
        }
       
        int[] answer = new int[deque.size()];
        int idx = 0;
        for (int d: deque) {
            answer[idx++] = d;
        }
        return answer;
    }
}