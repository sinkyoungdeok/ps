def solution(dartResult):
    answer = 0
    num = ''
    res = []
    
    for i in dartResult:
        if i.isnumeric():
            num += i 
        elif i == 'S':
            res.append(int(num))
            num = ''
        elif i == 'D':
            res.append(int(num)**2)
            num = ''
        elif i == 'T':
            res.append(int(num)**3)
            num = ''
        elif i == '*':
            if len(res) > 1:
                res[-1] = res[-1] * 2
                res[-2] = res[-2] * 2
            else:
                res[-1] = res[-1] * 2
        elif i == '#':
            res[-1] *= -1
            
    return sum(res)