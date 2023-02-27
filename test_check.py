#task1

list_value = [None, 3, None, 5, None, None, 14]
none_indexes = [i for i in range(len(list_value)) if list_value[i] is None]
print("The original list :", list_value)
print("The None indexes list is :", none_indexes)

#task2

boolean_list = [True, True, False, True, True, False, False, True] 
true_indexes = []
false_indexes = []

for i, value in enumerate(boolean_list):
    if value:
        true_indexes.append(i)
    else:
        false_indexes.append(i)

print("The original list is :", boolean_list)
print("True indexes after grouping", true_indexes)
print("False indexes after grouping", false_indexes)

#task3
def count_symbols(word):
# Check if input is valid
    if not isinstance(word, str):
        return False

    # Initialize an empty dictionary to store the results
    result = {}

    # Loop over each character in the word
    for char in word:
        # If the character is not already in the dictionary, add it with a count of 1
        if char not in result:
            result[char] = 1
        # If the character is already in the dictionary, increment its count by 1
        else:
            result[char] += 1

    # Return the final result
    return result
print("Task3")
print(count_symbols("abracadabra"))