t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    possible = True
    prev = 0

    for i in range(n - 1):
        need = prev + 1

        if a[i] < need:
            possible = False
            break

        extra = a[i] - need
        a[i + 1] += extra
        prev = need

    if possible and a[-1] > prev:
        print("YES")
    else:
        print("NO")

