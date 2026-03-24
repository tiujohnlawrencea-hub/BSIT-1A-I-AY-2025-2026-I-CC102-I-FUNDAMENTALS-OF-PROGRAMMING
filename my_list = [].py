my_list = []

# Fill the list from 1 to 9
for i in range(1, 10):
    my_list.append(i)

print("Original list:", my_list)
print("Length of list:", len(my_list))

y = 0

# Loop through list and ensure uniqueness
for x in range(len(my_list)):
    if y == len(my_list):
        break
    else:
        if my_list[x] not in my_list[:x]:
            y = y + 1
        else:
            del my_list[x]
            break

print("\nThe list with unique elements only.")
print(my_list)