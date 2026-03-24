n = int(input())


C = [[0]*n for _ in range(n)]

for i in range(n-1):
    row = list(map(int, input().split()))
    for j in range(i+1, n):
        C[i][j] = row[j - i - 1]

found = False

for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            if C[a][b] + C[b][c] < C[a][c]:
                found = True
                break
        if found:
            break
    if found:
        break

print("Yes" if found else "No")