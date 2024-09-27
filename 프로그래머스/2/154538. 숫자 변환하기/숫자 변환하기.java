import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        int[] dp = new int[y+1];
        
        for (int i=x;i<y+1;i++) {
            if (i!=x && dp[i] == 0) {
                dp[i] = -1;
                continue;
            }
            
            if (i+n < y+1) {
                dp[i+n] = (dp[i+n]==0) ? dp[i]+1 : Math.min(dp[i]+1,dp[i+n]);
            }
            
            if (i*2 < y+1) {
                dp[i*2] = (dp[i*2]==0) ? dp[i]+1 : Math.min(dp[i]+1,dp[i*2]);
            }
            
            if(i*3 < y+1) {
                dp[i*3] = (dp[i*3]==0) ? dp[i]+1 : Math.min(dp[i]+1,dp[i*3]);
            }
        }     
        
        return dp[y];
    }
}