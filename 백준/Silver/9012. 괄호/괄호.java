import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	int n = Integer.parseInt(br.readLine());
    	Stack<Character> stack;
    	StringBuilder sb = new StringBuilder();
    	
    	for (int i=0;i<n;i++) {
    		String answer = "YES";

    	 	stack = new Stack<>();
    		String input = br.readLine();
    		
    		for (int j=0;j<input.length();j++) {
    			char c = input.charAt(j);
    			
    			if (c=='(') {
    				stack.push(c);
    			} else if (stack.isEmpty()) {
    				answer = "NO";
    				break;
    			} else {
    				if (stack.peek() == '(') {
    					stack.pop();
    				}
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