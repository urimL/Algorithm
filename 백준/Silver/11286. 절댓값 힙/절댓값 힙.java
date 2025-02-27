import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	StringBuilder sb = new StringBuilder();
    	
    	PriorityQueue<int[]> q = new PriorityQueue<>((a,b) -> {
    		if (a[0] == b[0]) return a[1]-b[1];
    		return a[0] - b[0];
    	});
    	
    	for(int i=0;i<n;i++) {
    		//q -> {절대값, 실제값}
    		int v = Integer.parseInt(br.readLine());
    		int abs = Math.abs(v);
    		
    		if (v==0) {
    			if (q.isEmpty()) {
    				sb.append(0).append("\n");
    				continue;
    			}
    			
    			int[] result = q.poll();
    			sb.append(result[1]).append("\n");
    		
    		} else {
    			q.offer(new int[] {abs,v});
    		}
    		
    	}
    	
    	System.out.println(sb);
    
    }
}