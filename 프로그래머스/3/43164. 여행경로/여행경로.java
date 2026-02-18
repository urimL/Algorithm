import java.util.*;

class Solution {
    static boolean[] visited;
    static String[] answer;
    static boolean found;
    
    public String[] solution(String[][] tickets) {
                
        visited = new boolean[tickets.length];
        answer = new String[tickets.length+1];
        found = false;
        
        // 도착지 기준 정렬
        Arrays.sort(tickets, (a,b) -> {
            if (!a[0].equals(b[0])) return a[0].compareTo(b[0]);
            return a[1].compareTo(b[1]);
        });

        
        answer[0] = "ICN";
        dfs("ICN", tickets, 0);
        return answer;
        
    }
    
    static void dfs(String now, String[][] tickets, int depth) {
        if (found) return;
        
        if (depth == tickets.length) {
            found = true;
            return;
        }
        
        for (int i=0;i<tickets.length;i++) {
            if (!visited[i] && now.equals(tickets[i][0])) {
                answer[depth+1] = tickets[i][1];
                visited[i] = true;
                dfs(tickets[i][1], tickets, depth+1);
                
                if (found) return;
                visited[i] = false;
            }
        }
    }
}