import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int i = 0;
        
        for (int[] c: commands) {
            int start = c[0]-1; int end = c[1]; int idx = c[2]-1;
            int[] tmp = Arrays.copyOfRange(array, start, end);
            Arrays.sort(tmp);
            answer[i++] = tmp[idx];
        }
        
        
        return answer;
    }
}