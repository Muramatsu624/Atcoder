N = int(input())
S = [input() for i in range(N)]

for i in range(N):
    for j in range(N):
        if(i==j):
            continue
        ans = S[i] + S[j]
        if ans == ans[::-1] :
            print("Yes")
            exit()
print("No")

