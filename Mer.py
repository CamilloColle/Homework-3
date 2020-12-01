with open('rosalind_mer.txt') as f:
    n = int(f.readline())
    arr1 = list(map(int, f.readline().split()))
    m = int(f.readline())
    arr2 = list(map(int, f.readline().split()))

lst = []


def mer(arr1, arr2):

    while len(arr1) > 0 or len(arr2) > 0:

        if len(arr2) == 0:
            lst.append(arr1[0])
            arr1.remove(arr1[0])

        elif len(arr1) == 0:
            lst.append(arr2[0])
            arr2.remove(arr2[0])

        elif arr1[0] < arr2[0]:
            lst.append(arr1[0])
            arr1.remove(arr1[0])

        elif arr2[0] < arr1[0]:
            lst.append(arr2[0])
            arr2.remove(arr2[0])

        elif arr1[0] == arr2[0]:
            lst.append(arr1[0])
            lst.append(arr2[0])
            arr1.remove(arr1[0])
            arr2.remove(arr2[0])

    if len(arr1) == 0 and len(arr2) == 0:
        return lst


print(*mer(arr1, arr2))