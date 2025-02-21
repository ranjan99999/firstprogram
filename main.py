a = ['abc', '123', 'hello', '23', 95, 88]
empty_list = []
for item in a:
    if isinstance(item,int) or isinstance(item,str) and item.isdigit():
        empty_list = item + empty_list
print(empty_list)
