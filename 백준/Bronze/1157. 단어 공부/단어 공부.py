word = input().upper()
lst = list(set(word))
cnt_lst = []

if len(lst) == 1:
    print(lst[0])
else:
    for i in lst:
        cnt_lst.append(word.count(i))
    if cnt_lst.count(max(cnt_lst)) == 1:
        print(lst[cnt_lst.index(max(cnt_lst))])
    else:
        print('?')