import java.util.*;
class Solution {
    static ArrayList<Integer>[] edge;
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        edge = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            edge[i] = new ArrayList<>();
        }
        
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                if (i==j) continue;
                if (computers[i][j] == 1) {
                    edge[i].add(j);
                    edge[j].add(i);
                }
            }
        }
        
        for (int i=0;i<n;i++) {
            if (!visited[i]) {
                bfs(i);
                answer++;
            }
        }
        return answer;
    }
    
    private static void bfs(int now) {
        Queue<Integer> q = new ArrayDeque<>();
        visited[now] = true;
        q.add(now);
        
        while (!q.isEmpty()) {
            int x = q.poll();
            for (int nxt: edge[x]) {
                if (!visited[nxt]) {
                    visited[nxt]=true;
                    q.add(nxt);
                }
            }
        }
    }
}