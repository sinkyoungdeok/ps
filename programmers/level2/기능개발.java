import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        List<Integer> ans = new ArrayList<>();
        
        int date = 0;
        int i =0;
        int day = 0;
        
        while (i < progresses.length) {
            int progress = progresses[i];
            int speed = speeds[i];
            
            if(progress + date * speed >= 100) {
                i ++;
                day ++;
            } else if ( day > 0) {
                ans.add(day);
                day = 0;
                date ++;
            } else {
                date ++;
            }
        }
        ans.add(day);
        
        
        
        int[] answer = new int[ans.size()];
        for(int j=0; j< ans.size() ; j++ ){
            answer[j] = ans.get(i);
        }
        
        return answer;
    }
}