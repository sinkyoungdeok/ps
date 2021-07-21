import java.util.*;
class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        ArrayList<Integer> alphabetList = new ArrayList<>();
        
        for(int i=65; i<=90; i++) {
            char charI = (char)i;
            int cnt = 0 ;
            for(int j=0; j<skill.length(); j ++ ) {
                if(skill.charAt(j) == charI) 
                    cnt ++;
            }
            alphabetList.add(cnt);
        }
        
        for(int i=0; i< skill_trees.length; i++) {
            String newSkill = "";
            
            for(int j=0; j< skill_trees[i].length(); j++) {
                if(alphabetList.get(skill_trees[i].charAt(j) - 'A') == 1) {
                    newSkill += skill_trees[i].charAt(j);
                }
            }
            skill_trees[i] = newSkill;
        }
        
        
        for(String skillTree : skill_trees) {
            if(skillTree.length() == 0 ) {
                answer ++;
            } else {
                int k =0;
                answer ++;
                for(int j=0; j <skillTree.length();j++) {
                    if(skillTree.charAt(j) == skill.charAt(k) ) k ++;
                    else {
                        answer --;
                        break;
                    }
                }
            }
        }
        
        return answer;
    }
}