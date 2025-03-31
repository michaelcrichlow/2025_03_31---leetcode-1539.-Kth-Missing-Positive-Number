# leetcode 1539. Kth Missing Positive Number
# NOTE: All solutions passed, but Solution 03 is the fastest.

# Solution 01
def findKthPositive_00(arr: list[int], k: int) -> int:
    local_array = []
    num = 1
    while len(local_array) < k:
        if num not in arr:
            local_array.append(num)
        num += 1

    if len(local_array) >= 1:
        return local_array[-1]
    return 0


# Solution 02
def findKthPositive_01(arr: list[int], k: int) -> int:
    res = 0
    count = 0
    num = 1
    while count < k:
        if num not in arr:
            count += 1
            res = num
        num += 1

    return res


# Solution 03
def findKthPositive(arr: list[int], k: int) -> int:
    for val in arr:
        if val <= k:
            k += 1

    return k


def main() -> None:
    print(findKthPositive(arr = [2,3,4,7,11], k = 5))   # 9
    print(findKthPositive(arr = [1,2,3,4], k = 2))      # 6


if __name__ == '__main__':
    main()

