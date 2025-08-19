def findLeaders(arr):
    n = len(arr)
    leaders = []
    
    # Rightmost element is always a leader
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    # Traverse from second last to first element
    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    # Leaders are collected in reverse order
    leaders.reverse()
    return leaders
  
print("Input: [16, 17, 4, 3, 5, 2] => Leaders:", findLeaders([16, 17, 4, 3, 5, 2]))
print("Input: [1, 2, 3, 4, 0] => Leaders:", findLeaders([1, 2, 3, 4, 0]))
print("Input: [17, 10, 4, 10, 6, 5, 2] => Leaders:", findLeaders([17, 10, 4, 10, 6, 5, 2]))
print("Input: [5] => Leaders:", findLeaders([5]))
print("Input: [100, 50, 20, 10] => Leaders:", findLeaders([100, 50, 20, 10]))
print("Input: [1, 2, 3, ..., 1000000] => Leaders:", findLeaders(list(range(1, 1000001))))
