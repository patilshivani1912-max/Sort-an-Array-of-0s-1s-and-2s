import math

def lcm(n, m):
    return (n * m) // math.gcd(n, m)

print(lcm(4, 6))        
print(lcm(5, 10))       
print(lcm(7, 3))        
print(lcm(1, 987654321))
print(lcm(123456, 789012)) 
