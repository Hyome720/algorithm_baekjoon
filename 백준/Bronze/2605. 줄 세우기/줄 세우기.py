n = int(input())
order = list(map(int, input().split()))
order_lst = []

students = []

for i in range(1, n + 1):
    order_lst += [[i, order[i - 1]]]

for i in range(n):
    students.insert(len(students) - order_lst[i][1], order_lst[i][0])

print(*students)