def find_zero_sum_subarrays(arr):
    n = len(arr)
    prefix_sum = 0
    sum_map = {0: [-1]}  # handle subarrays starting at index 0
    result = []

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum in sum_map:
            for start in sum_map[prefix_sum]:
                result.append((start + 1, i))

        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = []
        sum_map[prefix_sum].append(i)

    return result


def print_results(arr):
    result = find_zero_sum_subarrays(arr)
    total = len(result)

    print(f"\nArray size: {len(arr)}")
    print(f"Total zero-sum subarrays: {total}")

    if total <= 20:  # Small test case → print all subarrays
        print("Subarrays:", result)
    else:  # Large test case → print summary only
        print("First 10 subarrays:", result[:10])
        print("Last 10 subarrays:", result[-10:])


#  Test Cases
print_results([4, -1, -3, 1, 2, -1])
print_results([1, 2, 3, 4])
print_results([0, 0, 0])
print_results([-3, 1, 2, 3, 4, 0])
arr = [1, -1, 2, -2, 3, -3] * 10000
print_results(arr)
          
