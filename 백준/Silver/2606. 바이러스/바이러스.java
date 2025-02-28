import java.util.*;
import java.io.*;

public class Main{
	static List<List<Integer>> map = new ArrayList<>();
	static boolean[] visited;
	static int answer = 0;
	
	public static void bfs(int node) {
		Queue<Integer> q = new LinkedList<>();
		q.add(node);
		visited[node] = true;
		
		while (!q.isEmpty()) {
			int now = q.poll();
			
			for (int n: map.get(now)) {
				if (!visited[n]) {
					visited[n] = true;
					answer++;
					q.add(n);
				}
			}
		}
	}
		
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	int n = Integer.parseInt(br.readLine());
    	int m = Integer.parseInt(br.readLine());
    	
    	visited = new boolean[n+1];
    	map = new ArrayList<>();
    	for (int i=0;i<=n;i++) map.add(new ArrayList<>());
    	
    	for(int i=0;i<m;i++) {
    		st = new StringTokenizer(br.readLine());
    		int s = Integer.parseInt(st.nextToken())-1;
    		int e = Integer.parseInt(st.nextToken())-1;
    		
    		map.get(e).add(s);
    		map.get(s).add(e); 		
    	}
    	
    	bfs(0);
    	System.out.println(answer);
    	
    }
}