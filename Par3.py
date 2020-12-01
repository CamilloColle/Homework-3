with open("rosalind_par3.txt") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))


def par3(arr):
    q = arr[0]
    L = []
    E = []
    H = []

    for i in arr:
        if i < q:
            L.append(i)
        elif i == q:
            E.append(i)
        elif i > q:
            H.append(i)

    return L + E + H


print(*par3(arr))
