N = int(input())
A = list(map(int, input().split()))
cnt = [0] * N
ans = ""
for i in range(3*N):
    cnt[A[i] -1] += 1
    if cnt[A[i] -1] == 2:
        ans += str(A[i]) + " "

print(ans)