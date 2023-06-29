H, W = map(int, input().split())
S = []
for i in range(H):
    S.append([])
    s = input()
    for j in range(W):
        S[i].append(s[j])

tate = []
yoko = []


for i in range(H):
    if "#" not in S[i]:
        continue
    else:
        tate.append(i)
for j in range(W):
    #listのj列目を抽出
    if "#" not in [row[j] for row in S]:
        continue
    else:
        yoko.append(j)

for i in tate:
    for j in yoko:
        if(S[i][j] == "."):
            print(f"{i+1} {j+1}")
            exit()






