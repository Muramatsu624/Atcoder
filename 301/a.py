game_num = int(input())

result = input()

takahasi = 0
aoki = 0
win_num = (game_num + 1) // 2 #必要な勝利数

for i in range(game_num):
    if(result[i] == "T"):
        takahasi += 1
        if takahasi == win_num:
            print("T")
            break
    else:
        aoki+= 1
        if aoki == win_num:
            print("A")
            break



