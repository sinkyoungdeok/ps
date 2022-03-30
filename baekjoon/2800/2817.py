X = int(input())

N = int(input())

staff_list = []
res = []
for _ in range(N):
    staff, vote = input().split()
    vote = int(vote)

    if vote / X * 100 >= 5.00:
        vote_list = []
        for i in range(14, 0, -1):
            vote_list.append(vote//i)
        staff_list.append((staff,vote_list))
        res.append([staff,0])

staff_len = len(staff_list)


for i in range(14):
    max_index, max_value = -1, 0

    for j in range(staff_len):
        if staff_list[j][1][-1] > max_value:
            max_index = j
            max_value = staff_list[j][1][-1]

    res[max_index][1] += 1
    staff_list[max_index][1].pop()

res.sort()

for staff, cnt in res:
    print(staff, cnt)



