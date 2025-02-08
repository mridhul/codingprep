def is_palindrome_simple(s):
    return s==s[::-1]

def is_palindrome_hard(s):
    left,right=0,len(s)-1
    while left < right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True





#test the simple palindrome
print(is_palindrome_simple("liril"))
print(is_palindrome_simple("santhoor"))

#test the hard palindrome
print(is_palindrome_hard("liril"))
print(is_palindrome_hard("santhoor"))