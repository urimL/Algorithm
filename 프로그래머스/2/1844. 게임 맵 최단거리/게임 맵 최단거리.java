import java.util.*;

class Solution {
    static int n;
    static int m;
    static boolean[][] visited;
    
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        visited = new boolean[n][m];
        int answer = bfs(new int[]{0,0}, maps);            
        
        return answer;
    }
    
    static int bfs(int[] now,int[][] maps) {
        Queue<int[]> q = new ArrayDeque<>();
        int[] dx = {1,-1,0,0}; int[] dy = {0,0,1,-1};
        q.add(now);
        visited[0][0] = true;
        
        while (!q.isEmpty()) {
            int[] tmp = q.poll();
            int x = tmp[0]; int y = tmp[1];
            
            for (int i=0;i<4;i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;
                
                if (0<=nx && nx<n && 0<=ny && ny<m && maps[nx][ny]==1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    maps[nx][ny] = maps[x][y] + 1;
                    q.add(new int[]{nx,ny});
                }
            }
        }
        
        return visited[n-1][m-1] ? maps[n-1][m-1] : -1;
    }
}