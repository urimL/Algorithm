import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	String[][] arr = new String[n][3];
    	
    	StringTokenizer st;
    	for (int i=0;i<n;i++) {
    		st = new StringTokenizer(br.readLine());
    		arr[i][0] = st.nextToken();
    		arr[i][1] = st.nextToken();
    		arr[i][2] = Integer.toString(i);
    	}
    	
    	StringBuilder sb = new StringBuilder();
    	Arrays.sort(arr, (e1, e2) -> {
    		if (e1[0].equals(e2[0])) {
    			return Integer.parseInt(e1[2])-Integer.parseInt(e2[2]);
    		} else {
    			return Integer.parseInt(e1[0])-Integer.parseInt(e2[0]);
    		}
    	});
    	
    	for (int i=0;i<n;i++) {
    		sb.append(arr[i][0] + " " + arr[i][1]).append("\n");
    	}
    	
    	System.out.println(sb.toString());
    }
}