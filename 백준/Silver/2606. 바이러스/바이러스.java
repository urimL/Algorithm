import java.util.*;
import java.io.*;

public class Main{
	static int[][] map;
	static boolean[] visited;
	static int answer = 0;
	
	public static void bfs(int node) {
		Queue<Integer> q = new LinkedList<>();
		q.add(node);
		visited[node] = true;
		
		while (!q.isEmpty()) {
			int now = q.poll();
			
			for (int i=0;i<map.length;i++) {
				if (map[now][i] == 1 && !visited[i]) {
					visited[i] = true;
					answer++;
					q.add(i);					
				}
			}
		}
	}
		
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	int n = Integer.parseInt(br.readLine());
    	int m = Integer.parseInt(br.readLine());
    	map = new int[n+1][n+1];
    	visited = new boolean[n+1];
    	
    	for(int i=0;i<m;i++) {
    		st = new StringTokenizer(br.readLine());
    		int s = Integer.parseInt(st.nextToken())-1;
    		int e = Integer.parseInt(st.nextToken())-1;
    		
    		map[s][e] = map[e][s] = 1;    		
    	}
    	
    	bfs(0);
    	System.out.println(answer);
    	
    }
}