t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    for i in a:
        if b.get(i) == None:
            b[i] = 1
        else:
            b[i] += 1
    for i in b:
        if b[i] % 2 != 0:
            print(i)
            break
        
