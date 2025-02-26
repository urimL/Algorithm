import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int n = Integer.parseInt(st.nextToken());
    	int m = Integer.parseInt(st.nextToken());
    	
    	int[] arr = new int[n];
    	for (int i=0;i<n;i++) {
    		arr[i] = i+1;
    	}
    	
    	for (int i=0;i<m;i++) {
    		st = new StringTokenizer(br.readLine());
    		int f = Integer.parseInt(st.nextToken())-1;
    		int s = Integer.parseInt(st.nextToken())-1;
    		
    		int tmp = arr[f];
    		arr[f] = arr[s];
    		arr[s] = tmp;
    		
    	}
    	
    	StringBuilder s = new StringBuilder();
    	for (int v: arr) {
    		s.append(v).append(" ");
    	}
    	System.out.println(s.toString().trim());
    }
}