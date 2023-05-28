import numpy as np

h, w = map(int, input().split())
#h行、任意の数の数値を入力
#list_a = [input().split() for i in range(h)]
#list_b = [input().split() for i in range(h)]

list_a = []
for i in range(h):
    list_a.append(input())
list_b = []
for i in range(h):
    line = input()
    list_b.append([])
    for j in range(w):
        list_b[i].append(line[j])

#print(list_a)
"""
def t_shift(a, h, bh):
    shifted = []
    for i in range(h):
        shifted.append(a[(i+bh) % h])
    return shifted

def y_shift(a, h, w, bw):
    shifted = [[] for i in range(h)]
    for i in range(h):
        for j in range(w):
            shifted[i].append(a[i][(j+bw) % w])
    return shifted

judge = -1

for i in range(h):
    for j in range(w):
        shifted = t_shift(list_a, h, i+1)
        shifted = y_shift(shifted, h, w, j+1)
        if (shifted == list_b):
            judge = 1

if(judge == 1):
    print("Yes")
else:
    print("No")
"""

judge = 0

for s in range(h):
    row_n = 0
    
    for t in range(w):
        array = []
        for i in range(h):
            list = []
            for j in range(w):
                list.append(list_a[(i+s)%h][(j+t)%w])
            array.append(list)
        #print(array)
        #print("-----------")
        if array == list_b:
            print("Yes")
            exit()
#print(list_b)
print("No")

