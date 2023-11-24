S = input() + ':'

num, string = ''.join(sorted(S)).split(':')
string += str(sum(list(map(int,list(num)))))

print(string)