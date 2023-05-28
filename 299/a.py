n = int(input())
s = input()

a_list = []
b_list = []

judge = 0

for i in range(n):
    if s[i] == "|":
        a_list.append(i)
    elif s[i] == "*":
        b_list.append(i)
    else: 
        continue

for i in range(len(a_list)-1):
    a = a_list[i]
    b = a_list[i+1]
    for j in range(len(b_list)):
        if(b_list[j] > a) and (b_list[j] < b):
            judge = 1

if(judge == 1):
    print("in")
else:
    print("out")

