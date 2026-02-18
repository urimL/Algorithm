import java.util.*;

class Solution {
    
    static class Node {
        String word;
        int depth;
        Node(String word, int depth) {
            this.word = word;
            this.depth = depth;
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        //words[] 안에 target 없는 경우
        boolean exist = false;
        for(String w: words) {
            if (w.equals(target)) {
                exist = true;
                break;
            }
        }
        if (!exist) return 0;
        
        boolean[] visited = new boolean[words.length];
        Queue<Node> q = new ArrayDeque<>();
        q.add(new Node(begin, 0));
        
        while (!q.isEmpty()) {
            Node now = q.poll();
            
            if (now.word.equals(target)) {
                return now.depth;
            }
            
            for (int i=0;i<words.length;i++) {
                if (!visited[i] && diff(now.word, words[i]) == 1) {
                    visited[i] = true;
                    q.add(new Node(words[i], now.depth+1));
                }
            }
        }
        
        return 0;
    }
    
    private static int diff(String a, String b) {
        int diff = 0;
        for(int i=0;i<a.length();i++) {
            if (a.charAt(i) != b.charAt(i)) diff++;
        }
        
        return diff;
    }
}