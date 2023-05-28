data_num = int(input())
data_row = list(map(int, input().split()))

answear = ""

for i in range(data_num-1):
    a = data_row[i]
    b = data_row[i+1]
    answear += str(a)
    answear += " "        
    if(a > b):     
        for j in reversed(range(b+1, a)):
            answear += str(j)
            answear += " "
    elif(a < b):
        for j in range(a+1, b):
            answear += str(j)
            answear += " "
    else:
        continue
    
answear += str(data_row[data_num-1])
print(answear)







