list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2
print(list3)
list3.pop(0)
print(list3)

def keep_list_at_size(x):
    if len(list3) < 5:
        list3.append(x)
        
    else:
        list3.pop(0)
        list3.append(x)

for i in range(5):
    keep_list_at_size("Good")
    print(list3)