# the `list.sort()` method sorts the list in place, which means it modifies the original list and returns `None`. Therefore, in your code, the `basket` variable is reassigned to `None`, not the sorted list. 

basket = [1, 5, 5, 3, 90, 56, 34, 23]

# Use the sort() method to sort the list in place, no need to reassign
basket.sort()

# Print the sorted list
print(basket)


# If you want to keep the original list and create a sorted copy, use the `sorted()` function.

basket = [1, 5, 5, 3, 90, 56, 34, 23]

# Use the sorted() function to create a sorted copy
sorted_basket = sorted(basket)

# Print the sorted copy
print(sorted_basket)

# Print the original list (unsorted)
print(basket)
