def decode_message(message):
     stack = []
     decoded_message = ""
     
     for char in message:
         if char == '*':
          if stack:
            decoded_message += stack.pop()
         else:
          stack.append(char)
    
     while stack:
        decoded_message += stack.pop()
     return decoded_message

message = "SIVLE ****** DAED TNSI ***"
decoded_message = decode_message(message)
print(decoded_message) 