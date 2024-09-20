import java.util.*;

class Solution {
    int[] dx = {-1,0,1,0};
    int[] dy = {0,-1,0,1};
    
    public int solution(int[][] maps) {
        
        int answer = 0;
        int[][] visited = new int[maps.length][maps[0].length];
        bfs(0,0,maps,visited);
        answer = visited[maps.length - 1][maps[0].length - 1];
        
        if (answer == 0) {
           answer = -1;
        }
        return answer;
    }
        
    public void bfs(int a,int b, int[][] maps,int[][] visited) {
        Queue<int[]> q = new LinkedList<>();

        q.add(new int[]{0,0});
        visited[a][b] = 1;
        while (!q.isEmpty()) {
            int[] now = q.poll();
            int x = now[0];
            int y = now[1];

            for (int i=0;i<4;i++) {
                int nx = dx[i] + x;
                int ny = dy[i] + y;

                if (nx < 0 || nx > maps.length-1 || ny < 0 || ny > maps[0].length-1) {
                continue;
                }

                if (visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                    visited[nx][ny] = visited[x][y]+1;
                    q.add(new int[]{nx,ny});
                }

            }
        }
    }
}