N = int(input())
A = list(map(int,input().split()))


ans = ""
for i in range(N):
    b = A[7*i:7*(i+1)]
    ans += str(sum(b)) + " "
print(ans)




