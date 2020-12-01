with open("rosalind_fibo.txt") as f:
    n = int(f.readline())


def fibo(n):
    x = 0
    prev2 = 0
    prev1 = 1
    for i in range(n):
        prev2 = prev1
        prev1 = x
        x = prev1 + prev2
    return x


print(fibo(n))

