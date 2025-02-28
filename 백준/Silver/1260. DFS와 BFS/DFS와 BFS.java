import java.util.*;
import java.io.*;

public class Main{
	
	static int[][] graph;
	static boolean[] visited;
	
	public static void dfs(int node) {
		visited[node] = true;
		System.out.print(node+" ");
		
		if (node > graph.length -1) {
			return;
		}
		
		for (int i=1;i<graph.length;i++) {
			if (graph[node][i] == 1 && !visited[i]) {
				dfs(i);
			}
		}
 	}
	
	public static void bfs(int start) {
		Queue<Integer> q = new LinkedList<>();
		q.add(start);
		visited[start] = true;
		System.out.print(start+" ");
		
		while(!q.isEmpty()) {
			int now = q.poll();
			for (int n=1; n<graph[now].length;n++) {
				if (!visited[n] && graph[now][n] == 1) {
					visited[n] = true;
					q.add(n);
					System.out.print(n + " ");
				}
			}
		}
	}	
	
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int n = Integer.parseInt(st.nextToken());
    	int m = Integer.parseInt(st.nextToken());
    	int v = Integer.parseInt(st.nextToken());
    	graph = new int[n+1][n+1];
    	
    	for(int i=0;i<m;i++) {
    		st = new StringTokenizer(br.readLine());
    		int s = Integer.parseInt(st.nextToken());
    		int e =  Integer.parseInt(st.nextToken());
    		
    		graph[e][s] = graph[s][e] = 1;
    	}
    	
    	visited = new boolean[n+1];
    	dfs(v);
    	System.out.println();
    	visited = new boolean[n+1];
    	bfs(v);
  
    }
}