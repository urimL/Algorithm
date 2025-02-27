import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	Queue<Integer> q = new LinkedList<>();
    	
    	StringTokenizer st;
    	StringBuilder sb = new StringBuilder();
    	int last = 0;
    	
    	for (int i=0;i<n;i++) {
    		st = new StringTokenizer(br.readLine());
    		String cmd = st.nextToken();
    		
    		
    		if (cmd.equals("push")) {
    			int value = Integer.parseInt(st.nextToken());
        		last = value;
        		q.offer(value);
    		}
    		else if (cmd.equals("pop")) {
    			if (q.isEmpty()) 
    				sb.append(-1).append("\n");
    			else
    				sb.append(q.poll()).append("\n");
    		} else if (cmd.equals("size")) {
    			sb.append(q.size()).append("\n");
    		} else if (cmd.equals("empty")) {
    			if (q.isEmpty()) 
    				sb.append(1).append("\n");
    			else
    				sb.append(0).append("\n");
    		} else if (cmd.equals("front")) {
    			if (q.isEmpty()) 
    				sb.append(-1).append("\n");
    			else
    				sb.append(q.peek()).append("\n");
    		} else if (cmd.equals("back")) {
    			if (q.isEmpty()) 
    				sb.append(-1).append("\n");
    			else
    				sb.append(last).append("\n");
    		}
    		
    	}
    	
    	System.out.println(sb);
    	
    
    }
}