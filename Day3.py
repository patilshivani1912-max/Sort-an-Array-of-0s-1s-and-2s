def findDuplicate(arr):
    # Step 1: Find intersection point in cycle
    slow = arr[0]
    fast = arr[0]
    
    while True:
        slow = arr[slow]         # move 1 step
        fast = arr[arr[fast]]    # move 2 steps
        if slow == fast:
            break
    
    # Step 2: Find entrance to the cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow


# ----------- Testing -------------
print(findDuplicate([1, 3, 4, 2, 2]))   # Output: 2
print(findDuplicate([3, 1, 3, 4, 2]))   # Output: 3
print(findDuplicate([1, 1]))            # Output: 1
print(findDuplicate([1, 4, 4, 2, 3]))   # Output: 4
print(findDuplicate(list(range(1, 100000)) + [50000]))  # Output: 50000
