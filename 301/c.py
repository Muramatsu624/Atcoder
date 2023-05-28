import numpy as np

#未完

s = input()
t = input()

s_count = np.zeros(27)

t_count = np.zeros(27)

#SとTの文字数の差を保存
s_t_dif = np.zeros(27)

for i in range(len(s)):
    if s[i] == "@":
        s_count[26] += 1
    else:
        s_count[ord(s[i]) - ord("a")] += 1
    if t[i] == "@":
        t_count[26] += 1
    else:
        t_count[ord(t[i]) - ord("a")] += 1

dif_num = 0
at_list = ["a", "t", "c", "o", "d", "e", "r"]
at_num = []
for chr in(at_list):
    at_num.append(ord(chr) - ord("a"))
for i in range(27):
    s_t_dif[i] = abs(s_count[i] - t_count[i])
    if i not in at_num and s_t_dif[i] != 0:
        print("No")
        break

    if i != 26:
        dif_num += s_t_dif[i]
    print(i, ":", s_t_dif[i])


if dif_num > s_t_dif[26]:
    print("No")
else:
    print("Yes")

