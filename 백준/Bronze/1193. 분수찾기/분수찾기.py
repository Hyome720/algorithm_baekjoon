n = int(input())
line_s = 0
i = 0

while True:
    if (i + 1) * i / 2 + 1 > n:
        line_s = i * (i - 1) / 2
        break
    else:
        i += 1

first = int(n - line_s)
last = int(i + 1 - (n - line_s))

if i % 2:
    print(f'{last}/{first}')
else:
    print(f'{first}/{last}')
