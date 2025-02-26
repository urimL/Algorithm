import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	int[] arr = new int[n];
    	boolean check = true;
    	
    	for (int i = 0;i<n;i++) {
    		int k = Integer.parseInt(br.readLine());
    		arr[i] = k;
    	}
    	
    	Stack<Integer> stack = new Stack<>();
    	StringBuilder sb = new StringBuilder();
    	int cnt = 1;
    	for (int a: arr) {
    		while (cnt <= a) {
    			stack.push(cnt++);
    			sb.append("+").append("\n");
    		}
    		
    		if (stack.get(stack.size()-1) == a) {
    			stack.pop();
    			sb.append("-").append("\n");
    		} else {
    			check = false;
    			break;
    		}
    		
    	}
    	
    	if (check == true)
    		System.out.println(sb);
    	else
    		System.out.println("NO");
    }
}