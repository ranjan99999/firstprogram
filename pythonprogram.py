a = ['abc', '123', 'hello', '23', 95, 88]
# for item in a:
#     # if item.isdigit():
#         if isinstance(item, (int, float)):
#             print(item


# print(' '.join(str(x) for x in a if type(x) == int or type(x) == float))

numeric_values = []

# # Iterate through the list
# for item in a:
#     # Check if the item is an integer or a string containing only digits
#     if isinstance(item, int) or (isinstance(item, str) and item.isdigit()):
#         numeric_values.append(str(item))  # Convert to string for proper output format
#
# # Print the numbers separated by space
# print(" ".join(numeric_values))

empty_list = []
for item in a:
    if isinstance(item, int) or isinstance(item, str) and item.isdigit():
         empty_list.append (str(item))
print(" ".join(empty_list))
