f = open("rosalind_3sum.txt")
first = list(map(int, f.readline().split()))

k = int(first[0])
n = int(first[1])


def threeSum(nums):

    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]].append(i + 1)
        else:
            dict[nums[i]] = [i + 1]

    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                index_0 = dict[nums[i]][0]
                index_1 = dict[nums[l]][0]
                index_2 = dict[nums[r]][0]
                if nums[l] == nums[i]:
                    index_1 = dict[nums[i]][1]
                if nums[r] == nums[l]:
                    index_2 = dict[nums[l]][1]
                if nums[r] == nums[i]:
                    index_2 = dict[nums[i]][1]

                solution = [index_0, index_1, index_2]
                solution.sort()
                return solution

    return [-1]


for i in range(k):
    arr = list(map(int, f.readline().split()))
    print(*threeSum(arr))