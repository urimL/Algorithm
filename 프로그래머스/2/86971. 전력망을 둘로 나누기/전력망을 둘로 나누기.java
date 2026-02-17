import java.util.*;

class Solution {
    static ArrayList<Integer>[] graph;
    static int min;
    
    public int solution(int n, int[][] wires) {
        graph = new ArrayList[n+1];
        min = Integer.MAX_VALUE;
        
        for (int i=1;i<=n;i++) graph[i] = new ArrayList<>();
        
        for (int[] w: wires) {
            int s = w[0]; int e = w[1];
            graph[s].add(e);
            graph[e].add(s);
        }
        
        for (int[] w: wires) {
            int s = w[0]; int e = w[1];
            boolean[] visited = new boolean[n+1];
            
            graph[e].remove(Integer.valueOf(s));
            graph[s].remove(Integer.valueOf(e));
            
            int cnt = backtrack(1, visited);
            
            int diff = Math.abs(cnt - (n-cnt));
            min = Math.min(min, diff);
            
            graph[e].add(s);
            graph[s].add(e);
        }
        
        return min;
    }
    
    private static int backtrack(int v, boolean[] visited) {
        visited[v] = true;
        int cnt = 1;
        
        for (int next: graph[v]) {
            if (!visited[next]) 
                cnt += backtrack(next, visited);
        }
        
        return cnt;
    }
}