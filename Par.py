with open("rosalind_par.txt") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))


def par(arr):
    q = arr[0]
    L = []
    H = []
    for i in arr[1:]:
        if i < q:
            L.append(i)
        else:
            H.append(i)

    return L + [q] + H


print(*par(arr))