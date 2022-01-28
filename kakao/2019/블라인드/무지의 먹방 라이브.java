import java.util.*;

class Info implements Comparable<Info> {
    public int value;
    public int i;
    
    Info(int value, int i) {
        this.value = value;
        this.i = i;
    }
    
    @Override
    public int compareTo(Info info) {
        if(this.value > info.value) return 1;
        else if(this.value < info.value) return -1;
        else {
            if(this.i > info.value) return 1;
            else if(this.i < info.value) return -1;
            return 0;
        }
    }
    
}

class Solution {
    public int solution(int[] food_times, long k) {
        int answer = -1;
        
        PriorityQueue<Info> pq = new PriorityQueue<>();
        
        for(int i=0; i< food_times.length; i++) {
            pq.add(new Info(food_times[i], i+1));
        }
        
        int prev = 0;
        long food_len = food_times.length;
        List<Integer> list = new ArrayList<>();
        
        while (!pq.isEmpty()) {
            Info currInfo = pq.poll();
            
            long temp = (currInfo.value - prev) * food_len;
            
            if(k >= temp) {
                k -= temp;
                prev = currInfo.value;
                food_len -= 1;
            } else {
                pq.add(new Info(currInfo.value, currInfo.i));
                
                while (!pq.isEmpty()) {
                    Info te = pq.poll();
                    list.add(te.i);
                }
                
                Collections.sort(list);
                
                answer = list.get((int)(k % food_len));
                break;
            }
        }
        
        return answer;
    }
}