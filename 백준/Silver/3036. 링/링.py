t = int(input())
lst = list(map(int, input().split()))
for k in range(1, t):
    a, b = lst[0], lst[k]
    gop = a * b

    nums = []
    i = 2
    min_num = 1
    max_num = 1

    if a == b:
        print(f'1/1')
    else:
        while a > i or b > i:
            if a % i == 0 and b % i == 0:
                nums.append(i)
                a //= i
                b //= i
                i = 2
            else:
                i += 1
                if a == i or b == i:
                    nums.append(1)

        for i in nums:
            min_num *= i

        max_num = gop // min_num

        print(f'{lst[0] // min_num}/{lst[k] // min_num}')