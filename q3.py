def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    # Check if dct is a dictionary
    if not isinstance(dct, dict):
        return -1

    # If key exists, print the original value
    if key in dct:
        print("Original value:", dct[key])

    # Update or add the key-value pair
    dct[key] = value

    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"

my_dict = {}
print(update_dictionary (my_dict, "name", "Alice"))

# - {"age": 25}, "age", 26
my_dict = {"age": 25}
print(update_dictionary (my_dict, "age", 26))
