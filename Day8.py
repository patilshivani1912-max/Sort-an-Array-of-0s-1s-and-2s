def reverse_words(s: str) -> str:
    
    words = s.strip().split()
    
    words.reverse()
    
    return " ".join(words)

print(reverse_words("the sky is blue"))      
print(reverse_words("  hello world  "))      
print(reverse_words("a good   example"))     
print(reverse_words("   "))                  
print(reverse_words("word"))                 
