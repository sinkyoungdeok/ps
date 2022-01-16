import math

def solution(fees, records):
    answer = []
    
    car_dict = {}
    time_dict = {}
    
    end_time = 23 * 60 + 59
    
    for re in records:
        t, c, io = re.split()
        h, m = map(int,t.split(":"))
        time = h * 60 + m
        
        if io == "IN":
            car_dict[c] = time
        else:
            time = time - car_dict[c]    
            del car_dict[c]
            
            if time_dict.get(c):
                time_dict[c] += time
            else:
                time_dict[c] = time
    
    for k,v in car_dict.items():
        time = end_time - v
        if time_dict.get(k):
            time_dict[k] += time
        else:
            time_dict[k] = time
            
            
    base_time, base_fee, unit_time, unit_fee = fees
    
    temp = []
    for k,v in time_dict.items():
        if v <= base_time:
            res = base_fee
        else:
            res = base_fee + math.ceil((v-base_time) / unit_time) * unit_fee
        
        temp.append( (k,res))
        
    temp.sort()
    
    for i,j in temp:
        answer.append(j)
    
    return answer