list = [1, 2, 3, 4, 5]
# Demo on list comprehension
# 
# # List comprehension
# new_list = [new_item for item in list]
print([item * 2 for item in list])

# # List comprehension conditional
# new_list = [new_item for item in list if test]
print([item * 2 for item in list if item % 2 == 0])

dict = {"a": 1, "b": 2, "c": 3}
# Demo on dictionary comprehension
#
# # Dictionary comprehension
# new_dict = {new_key: new_value for item in dict.items()}
print({key: value * 2 for key, value in dict.items()})

# # Dictionary comprehension conditional
# new_dict = {new_key: new_value for item in list if test}
print({key: value * 2 for key, value in dict.items() if value % 2 == 0})

# Demo on string comprehension
#
# # String comprehension


# Demo on set comprehension
#
# # Set comprehension
# new_set = {new_item for item in list if test}


# Demo on generator expression
#
# # Generator expression
# new_list = (new_item for item in list if test)


# Demo on lambda function
#
# # Lambda function
# new_list = list(map(lambda item: new_item, list if test))


# Demo on filter function
#
# # Filter function
# new_list = list(filter(lambda item: new_item, list if test))


# Demo on zip function
#
# # Zip function
# new_list = list(zip(list, list))


# Demo on sorted function
#
# # Sorted function
# new_list = sorted(list)


# Demo on reversed function
#
# # Reversed function
# new_list = reversed(list)
