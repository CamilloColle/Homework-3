with open('rosalind_maj.txt') as f:
    first = list(map(int, f.readline().split()))

n = first[0]
m = first[1]
x = m//2

for i in range(n):
    arr = list(map(int, f.readline().split()))
    d={}
    z = -1
    for j in arr:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    for k in d:
        if d[k] > x:
            z = k
            break
    print(z, end = ' ')



