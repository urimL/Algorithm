import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	ArrayList<Integer> list = new ArrayList<>();
    	Scanner sc = new Scanner(System.in);
    	int n = sc.nextInt();
    	int m = sc.nextInt();
    	
    	for (int i=1;i<=n;i++) {
    		list.add(i);
    	}
    	
    	for (int i = 0;i<m;i++) {
    		int f = sc.nextInt() - 1;
    		int s = sc.nextInt() - 1;
    		
    		int tmp = list.get(f);
    		list.set(f, list.get(s));
    		list.set(s, tmp);
    	}
    	
    	for (int v : list) 
    		System.out.print(v + " ");
    	
    }
    
} 