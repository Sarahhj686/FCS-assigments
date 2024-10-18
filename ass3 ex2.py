def insert_value(sorted_list, value):
    start, end = 0, len(sorted_list)

    while start < end:
        mid = (start+end) // 2
        if sorted_list[mid] < value:
            start = mid + 1
        else:
            end = mid
    sorted_list.insert(start, value)

sorted_list = list(map(int, input("Enter integers separated by spaces (e.g., '1 2 3'): ").split()))
value=int(input("enter an integer you want to add to your list:"))
insert_value(sorted_list, value)
print(sorted_list)


            