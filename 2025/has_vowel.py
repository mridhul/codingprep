def has_vowel(s):
    for char in s:
        if char in "aeiou":
            return True
    return False

def has_vowels(s):
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            return True
    return False

# Example usage
print(has_vowels("hello"))  # True
print(has_vowels("rhythm"))  # False


#has vowel
print(has_vowel("mridhul"))
print(has_vowel("qwrtypl"))