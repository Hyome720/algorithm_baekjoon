n = int(input())
lst = []
num_s = 666

while len(lst) < n:
    str_num = str(num_s)
    for i in range(len(str(num_s)) - 2):
        if str_num[i] == str_num[i + 1] == str_num[i + 2] == '6':
            lst.append(num_s)
            break
    num_s += 1

print(lst[-1])