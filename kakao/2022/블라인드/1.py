def solution(id_list, report, k):
    cnt_dict = {}
    report_dict = {}
    answer = []

    for id in id_list:
        cnt_dict[id] = set()
        report_dict[id] = set()
        
    for r in report:
        s,d = r.split()
        
        cnt_dict[d].add(s)
        report_dict[s].add(d)
        
    for id in id_list:
        ans = 0
        for r in report_dict[id]:
            if len(cnt_dict[r]) >= k:
                ans+=1
                
        answer.append(ans)
    
    
    
    return answer