class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int x=0; int y=0;
        for(int[] s: sizes) {
            int tmpX = Math.max(s[0], s[1]);
            int tmpY = Math.min(s[0], s[1]);
            
            x = Math.max(x, tmpX);
            y = Math.max(y, tmpY);
        }
        
        return x*y;
    }
}