def isGood(s):
    left = 0
    right = 0
    stack = []
    for i in range(0, len(s)):
        if s[i] == "(":
            left += 1
            stack.append(s[i])
        else:
            right += 1
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if left == right and len(stack) == 0:
        return True
    else:
        return False

def convert(s):
    # 1
    if len(s) == 0:
        return s
    # 2
    left = 0
    right = 0
    if s[0] == "(":
        left +=1
    else:
        right += 1
    for i in range(1, len(s)):
        if s[i] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            break
    u = s[0:i+1]
    v = s[i+1:len(s)]
    # 3
    if isGood(u):
        v = convert(v)
        # 3-1
        u += v
        return u
    # 4
    else:
        # 4-1, 4-2, 4-3
        temp = "(" + convert(v) + ")"
        # 4-4
        u = u[1:-1]
        for i in u:
            if i == "(":
                temp += ")"
            else:
                temp += "("
        return temp

def solution(p):
    if isGood(p):
        return p
    answer = convert(p)
    return answer

p = "()))((()"
print(solution(p))