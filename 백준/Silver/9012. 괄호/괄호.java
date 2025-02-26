import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int n = Integer.parseInt(br.readLine());
    	Stack<Character> stack = new Stack<>();
    	StringBuilder sb = new StringBuilder();
    	
    	for (int i=0;i<n;i++) {
    		String answer = "YES";
    		String input = br.readLine();
    		stack.clear();
    		
    		for (char c : input.toCharArray()) {
    			
    			if (c=='(') {
    				stack.push(c);
    			} else if (stack.isEmpty()) {
    				answer = "NO";
    				break;
    			} else {
    				stack.pop();
    			}
    		}
    		
    		if (!stack.isEmpty()) {
    			answer = "NO";
    		}
    		sb.append(answer).append("\n");
    	}
    	
    	System.out.println(sb);
    }
}