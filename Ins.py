n= int(input())
arr = list(map(int, input().split()))
count = 0
x = arr[-1]

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            count += 1
        else:
            break


print(count)

