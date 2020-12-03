f = open('rosalind_maj.txt')
first = list(map(int, f.readline().split()))

k = first[0]
n = first[1]
x = n//2


def maj(arr):
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
    return z


for i in range(k):
    arr = list(map(int, f.readline().split()))
    print(maj(arr), end = ' ')

