f = open('rosalind_2sum.txt')
first = list(map(int, f.readline().split()))
k = first[0]
n = first[1]

pair_sum = 0


def sum(arr, target=0):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            return dict[arr[i]] + 1, i + 1
        else:
            dict[target - arr[i]] = i

    return [-1]


for i in range(k):
    arr = list(map(int, f.readline().split()))
    print(*sum(arr, target=0))