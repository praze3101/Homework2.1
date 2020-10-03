#a
list = [1, "Hello", True]
list_as_string = '' .join(str(i) for i in list)
print(list_as_string)
#b
list = [1, 1, 2, "Sorry", "For", "Delay"]
my_set = set(list)
my_unique_list = []
for i in my_set:
    if i not in my_unique_list:
        my_unique_list.append(i)
print(my_unique_list)

#c
