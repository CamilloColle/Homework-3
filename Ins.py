with open("rosalind_ins.txt") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))


def ins(arr, n):
    count = 0
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1

            else:
                break
    return count


print(ins(arr, n))

