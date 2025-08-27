def longest_palindrome_center(s: str) -> str:
    """Expand Around Center approach (O(n^2) time, O(1) space)"""
    if not s or len(s) == 0:
        return ""
    
    start, end = 0, 0

    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  

    for i in range(len(s)):
        len1 = expand_around_center(i, i)       
        len2 = expand_around_center(i, i + 1)   
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]


def longest_palindrome_dp(s: str) -> str:
    """Dynamic Programming approach (O(n^2) time, O(n^2) space)"""
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True
      
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length

    return s[start:start + max_len]

test_strings = ["babad", "cbbd", "a", "aaaa", "abc"]

for t in test_strings:
    print(f"Input: {t}")
    print(" Center Expansion:", longest_palindrome_center(t))
    print(" Dynamic Programming:", longest_palindrome_dp(t))
    print("-" * 40)
      
