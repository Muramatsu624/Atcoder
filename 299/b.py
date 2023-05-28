n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

if t in c:
    max = 0
    max_p = 0
    for i in range(len(c)):
        if (c[i] == t) and (r[i] > max):
            max = r[i]
            max_p = i+1
    print(max_p)
else:
    t = c[0]
    max = 0
    max_p = 0
    for i in range(len(c)):
        if (c[i] == t) and (r[i] > max):
            max = r[i]
            max_p = i+1
    print(max_p)







