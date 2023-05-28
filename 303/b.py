import itertools

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]



#all_list = list(itertools.combinations(n, 2))
#print(all_list)

cnt = 0

for num in range(n):
    flag = 0
    ans = []
    for i in range(m):
        for j in range(n):
            if(a[i][j] == num+1):
                if j == 0 and a[i][j+1] not in ans:
                    ans.append(a[i][j+1])
                elif j == n-1 and a[i][j-1] not in ans:
                    ans.append(a[i][j-1])
                elif(0 < j < n-1):
                    if a[i][j+1] not in ans:
                        ans.append(a[i][j+1])
                    if a[i][j-1] not in ans:
                        ans.append(a[i][j-1])
    #print(ans)
    cnt += (n - len(ans) - 1)
cnt /= 2
cnt = int(cnt)
print(cnt)









