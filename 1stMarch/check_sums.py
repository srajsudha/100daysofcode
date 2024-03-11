lst = [1, 5, 11, 5] 
k = 6

for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[i] +lst[j] == k:
            print(lst[i]) 
