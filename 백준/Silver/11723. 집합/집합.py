import sys

m = int(sys.stdin.readline().rstrip())
bit = 0

for _ in range(m):
    cmd = sys.stdin.readline().rstrip().split()
    if len(cmd) == 2:
        num = int(cmd[1]) - 1
        if cmd[0] == 'add':
            bit |= (1 << num)
        elif cmd[0] == 'remove':
            bit &= ~(1 << num)
        elif cmd[0] == 'check':
            if bit & (1 << num):
                print(1)
            else:
                print(0)
        elif cmd[0] == 'toggle':
            bit ^= (1 << num)
    else:
        if cmd[0] == 'all':
            bit = (1 << 20) - 1
        else:
            bit = 0