def is_palindrome(s):
    s = s.replace(" ", "").lower()
    stack = []
    for char in s:
        stack.append(char)
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    return s == reversed_s  
example=str(input("enter a word or sentence to check:"))
print(is_palindrome(example))


