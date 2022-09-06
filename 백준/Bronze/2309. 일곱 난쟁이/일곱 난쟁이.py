def func(idx, n, r, res):
    global height
    global lst
    if idx == r:
        if height == 100:
            lst = res[:]
            return
        return

    start = 0
    if res:
        start = max(res) + 1
        # start = max(res)  # +1이 없다면 중복 허용

    for i in range(start, n):
        if height - dwarf_lst[i] < 100:
            continue
        height -= dwarf_lst[i]
        res.append(i)
        func(idx + 1, n, r, res)
        height += dwarf_lst[i]
        res.pop()

        # func(idx+1, n, r , res + [i])

dwarf_lst = []
seven_dwarf = []
lst = []

for _ in range(9):
    a = int(input())
    dwarf_lst.append(a)
height = sum(dwarf_lst)


func(0, 9, 2, [])

del dwarf_lst[lst[0]]
del dwarf_lst[lst[1] - 1]

dwarf_lst.sort()

for i in range(7):
    print(dwarf_lst[i])