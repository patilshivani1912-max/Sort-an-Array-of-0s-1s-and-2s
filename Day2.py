def find_missing_number(arr):
    n = len(arr) + 1  # since one number is missing
    total = n * (n + 1) // 2  # sum of 1 to n
    arr_sum = sum(arr)
    return total - arr_sum


# Test Cases
print(find_missing_number([1, 2, 4, 5]))        # Output: 3
print(find_missing_number([2, 3, 4, 5]))        # Output: 1
print(find_missing_number([1, 2, 3, 4]))        # Output: 5
print(find_missing_number([1]))                 # Output: 2
print(find_missing_number(list(range(1, 1000000))))  # Output: 1000000
