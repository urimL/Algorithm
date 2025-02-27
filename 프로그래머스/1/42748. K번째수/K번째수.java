import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int idx = 0;
        
        for (int[] arr: commands) {
            int start = arr[0]-1; int end = arr[1]-1; int cnt = arr[2]-1;
            int[] tmp = new int[end-start+1];
            
            for (int i=start;i<=end;i++){
                tmp[i-start] = array[i];
            }
            
            Arrays.sort(tmp);
            answer[idx++] = tmp[cnt];
            
        }    
        return answer;
    }
}