import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
    	StringBuilder sb = new StringBuilder();
    	
    	for(int i=0;i<n;i++) {
    		int v = Integer.parseInt(br.readLine());
    		switch(v) {
    		case 0:
    			if (q.isEmpty()) 
    				sb.append(0).append("\n");
    			else
    				sb.append(q.poll()).append("\n");
    			break;
    		default:
    			q.offer(v);    			
    		}
    	}
    	
    	System.out.println(sb);
    
    }
}