def fibonacci(n: int) -> int:
    
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


print("Input: 5  -> Output:", fibonacci(5))      
print("Input: 10 -> Output:", fibonacci(10))     
print("Input: 0  -> Output:", fibonacci(0))      


print("Input: 1000 -> Output (integer):")
print(fibonacci(1000))


print("Input: 1000 -> Output (scientific notation):")
print(float(fibonacci(1000)))
