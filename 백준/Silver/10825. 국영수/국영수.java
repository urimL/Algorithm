import java.util.*;
import java.io.*;


public class Main{
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int n = Integer.parseInt(br.readLine());
    	HashMap<String, int[]> map = new HashMap<>();
    	List<Map.Entry<String, int[]>> list;
    	
    	StringTokenizer st;
    	for (int i = 0;i<n;i++) {
    		st = new StringTokenizer(br.readLine());
    		String name = st.nextToken();
    		
    		int[] score = new int[3];
    		score[0] = Integer.parseInt(st.nextToken());
    		score[1] = Integer.parseInt(st.nextToken());
    		score[2] = Integer.parseInt(st.nextToken());
    		
    		map.put(name, score);
    		
    	}
    	
    	list = new ArrayList<>(map.entrySet());
		list.sort((e1, e2) -> {
			if (e1.getValue()[0] == e2.getValue()[0]) {
				if (e1.getValue()[1] == e2.getValue()[1]) {
					if(e1.getValue()[2] == e2.getValue()[2]) {
						return e1.getKey().compareTo(e2.getKey());
					}
					return e2.getValue()[2] - e1.getValue()[2];
				} return e1.getValue()[1] - e2.getValue()[1];
			} return e2.getValue()[0]  - e1.getValue()[0];
		});
    	
    	StringBuilder sb = new StringBuilder();
    	
    	for(Map.Entry<String, int[]> e: list) {
    		sb.append(e.getKey()).append("\n");
    	
    	}
    	
    	System.out.println(sb);
    }
}