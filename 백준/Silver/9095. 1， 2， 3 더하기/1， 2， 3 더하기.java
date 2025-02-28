import java.util.*;
import java.io.*;

public class Main{
	static int[] dp;
	
    public static void main(String[] args) throws IOException{
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int t = Integer.parseInt(br.readLine());
    	dp = new int[12];
    	
    	for (int k=0;k<t;k++) {
	    	int n = Integer.parseInt(br.readLine());
	    	dp[1] = 1;
	    	dp[2] = 2;
	    	dp[3] = 4;
	    	
	    	for (int i=4;i<=n;i++) {
	    		dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
	    	}
	    	
	    	System.out.println(dp[n]);
    	}
    	
    }
}