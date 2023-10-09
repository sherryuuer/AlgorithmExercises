dictionary = dict()
dictionary = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print(dictionary)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

print(dictionary.keys())
# dict_keys(['one', 'two', 'three', 'four', 'five'])

print(dictionary.values())
# dict_values([1, 2, 3, 4, 5])

print(dictionary.items())
# dict_items([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)])

print(dictionary['one'])  # Accessing a value by its key in O(1) time
# 1

dictionary['six'] = 6  # Inserting the value 6 for the key 'six' in O(1) time.
print(dictionary)
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
