with open("rosalind_med.txt") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
    k = int(f.readline())

def med(arr, k):
    arr.sort(key = int)
    return arr[k-1]


print(med(arr,k))
