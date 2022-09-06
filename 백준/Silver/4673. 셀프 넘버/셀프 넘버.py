def self_num(n):
    if n <= 10000:
        n = n // 1000 % 10 + n // 100 % 10 + n // 10 % 10 + n % 10 + n
        if n < 10000:
            lst_set.add(n)
            self_num(n)
        elif n == 10000:
            lst_set.add(n)
            return lst_set
    else:
        return lst_set


num_lst = set(range(1, 10001))
lst_set = set()

for i in range(1, 10000):
    self_num(i)

a = list(num_lst - lst_set)
a.sort()

for i in a:
    print(i)