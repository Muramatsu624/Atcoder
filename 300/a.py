n, a, b = map(int,input().split())
list_a = list(map(int,input().split())) #任意の数の整数をリストして保存

c = a + b
for i in range(len(list_a)):
    if(c == list_a[i]):
        print(i+1)

