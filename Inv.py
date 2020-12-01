with open("rosalind_inv.txt") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))


def inv(arr):
    s_arr = sorted(arr)
    count = 0
    while len(arr) > 0:
        x = s_arr.index(arr[0])
        count += x

        s_arr.pop(s_arr.index(arr[0]))
        arr.pop(0)
    return count


print(inv(arr))