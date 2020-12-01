with open('rosalind_bins.txt') as f:
    max = int(f.readline())
    m = int(f.readline())
    arr = list(map(int, f.readline().split()))
    arrm = list(map(int, f.readline().split()))

min = 0


def bins(arr, i, min, max):
    if i in arr:
        c = (min + max)//2
        if i == arr[c]:
            return c + 1
        elif i < arr[c]:
            return bins(arr, i, min, c-1)
        elif i > arr[c]:
            return bins(arr, i, c+1, max)

    else:
        return -1

for j in arrm:
    print(bins(arr, j, min, max), end = ' ')