def binary_search(list1, key, start, end):
    if start <= end:
        mid = (start + end) // 2
        if list1[mid] == key:
            return mid
        elif list1[mid] > key:
            return binary_search(list1, key, start, mid - 1)
        else:
            return binary_search(list1, key, mid + 1, end)
    else:
        return "Key is not found"

list1 = list(map(int, input("Enter integers separated by spaces (e.g., '1 2 3'): ").split()))
key = int(input("Enter the key you want to search for: "))
result = binary_search(list1, key, 0, len(list1) - 1)
print(result)


    
