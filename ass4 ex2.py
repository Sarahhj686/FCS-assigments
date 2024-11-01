def is_balanced(expression):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map:
            if stack and stack[-1] == parentheses_map[char]:
                stack.pop()  
            else:
                return False 
    return len(stack) == 0
print(is_balanced("(1+2)-3*[41+6]"))        
print(is_balanced("(1+2)-3*[41+6}"))        
print(is_balanced("(1+2)-3*[41+6"))         
print(is_balanced("(1+2)-3*]41+6["))        
print(is_balanced("(1+[2-3]*4{41+6})"))     
  


