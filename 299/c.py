n = int(input())
s = input()

max_l = 0
cont_l = 0
if ("o" not in s) or ("-" not in s):
    print(-1)
else:
    for i in range(n):
        if s[i] == "o":
            cont_l += 1
        else:
            if(cont_l > max_l):
                max_l = cont_l
            cont_l = 0
    if(cont_l > max_l):
        max_l = cont_l
    print(max_l)





