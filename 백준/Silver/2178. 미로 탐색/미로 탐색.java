import java.util.*;
import java.io.*;

public class Main{
	static int[][] map;
	static int n,m;
	static boolean[][] visited;
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
	
	public static int bfs(int a, int b) {
		Queue<int[]> q = new LinkedList<>();
		q.add(new int[] {a,b});
		visited = new boolean[n+1][m+1];
		visited[a][b] = true;
		
		while (!q.isEmpty()) {
			int[] now = q.poll();
			int x = now[0];
			int y = now[1];
		
			for (int i=0;i<4;i++) {
				int nx = dx[i] + x;
				int ny = dy[i] + y;
				if (0>nx || 0>ny || n <= nx || m <= ny) continue;
				if (!visited[nx][ny] && map[nx][ny] == 1) {
					q.add(new int[] {nx,ny});
					map[nx][ny] = map[x][y] + 1;
					visited[nx][ny] = true;
				}
			}
		}
		return map[n-1][m-1];
	}
	
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	n = Integer.parseInt(st.nextToken());
    	m = Integer.parseInt(st.nextToken());
    	
    	map = new int[n+1][m+1];
    	
    	for (int i=0;i<n;i++) {
    		String s = br.readLine();
    		for (int j=0;j<m;j++) {
    			map[i][j] = s.charAt(j) - '0';
    		}		
    	}

    	System.out.println(bfs(0,0));
  
    }
}