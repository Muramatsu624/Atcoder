N = int(input())
S = []
A = []
for i in range(N):
    s = input().split()
    S.append(s[0])
    A.append(int(s[1]))

pos = A.index(min(A))
for i in range(N):
    print(S[pos])
    pos += 1
    if(pos == N):
        pos = 0








