import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        final String[] answer = {""};
        
        Map<String, Integer> dic = new HashMap<>();
        for(String p : participant) {
            if(dic.get(p) == null) {
                dic.put(p,1);
            } else {
                int val = dic.get(p) + 1;
                dic.put(p,val);
            }
        }
        
        for(String c : completion) {
            int val = dic.get(c) - 1;
            dic.put(c, val);
        }
        
        dic.forEach((k,v) -> {
            if(v == 1) answer[0] = k;
        });
        
        
        return answer[0];
    }
}