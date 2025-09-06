from collections import deque

def sliding_window_maximum(arr, k):
    dq = deque()
    result = []
    for i in range(len(arr)):
        
        if dq and dq[0] == i - k:
            dq.popleft()
        
        
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        
        dq.append(i)
        
        
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result

print(sliding_window_maximum([1, 5, 3, 2, 4, 6], 3))  
print(sliding_window_maximum([1, 2, 3, 4], 2))  
print(sliding_window_maximum([7, 7, 7, 7], 1))  
