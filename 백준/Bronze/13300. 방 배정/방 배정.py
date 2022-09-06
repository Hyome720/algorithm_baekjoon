n, k = map(int, input().split())
stud_lst = list(list(map(int, input().split())) for _ in range(n))
# print(stud_lst)

room = 0

grade_1_m = []
grade_1_w = []
grade_2_m = []
grade_2_w = []
grade_3_m = []
grade_3_w = []
grade_4_m = []
grade_4_w = []
grade_5_m = []
grade_5_w = []
grade_6_m = []
grade_6_w = []

for stud in stud_lst:
    if stud[1] == 1:
        if stud[0]:
            grade_1_m.append(stud)
        else:
            grade_1_w.append(stud)
    elif stud[1] == 2:
        if stud[0]:
            grade_2_m.append(stud)
        else:
            grade_2_w.append(stud)
    elif stud[1] == 3:
        if stud[0]:
            grade_3_m.append(stud)
        else:
            grade_3_w.append(stud)
    elif stud[1] == 4:
        if stud[0]:
            grade_4_m.append(stud)
        else:
            grade_4_w.append(stud)
    elif stud[1] == 5:
        if stud[0]:
            grade_5_m.append(stud)
        else:
            grade_5_w.append(stud)
    elif stud[1] == 6:
        if stud[0]:
            grade_6_m.append(stud)
        else:
            grade_6_w.append(stud)

grades = [[grade_1_m] + [grade_1_w]] + [[grade_2_m] + [grade_2_w]] + [[grade_3_m] + [grade_3_w]] + [[grade_4_m] + [grade_4_w]] + [[grade_5_m] + [grade_5_w]] + [[grade_6_m] + [grade_6_w]]

for a in grades:
    if len(a[0]) % k:
        room += (len(a[0]) // k) + 1
    else:
        room += len(a[0]) // k
    if len(a[1]) % k:
        room += (len(a[1]) // k) + 1
    else:
        room += len(a[1]) // k

print(room)