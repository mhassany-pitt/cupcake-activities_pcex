# Define a binary search function that also detects if the key in the given list.
def binary_search(data, key):
        found = False
        low = 0
        high = len(data)-1
        # Using while to conduct a search iteration
        while (not found and low <= high):
                guess = (high + low) // 2
                if (key == data[guess]):
                        found = True
                else:
                        if (key<data[guess]):
                                high = guess-1
                        else:
                                low = guess+1
        # After one of the while conditions is not satisfied anymore, we need to check if the key is found
        if not found:
                guess = -1
        return guess
data = [1, 5, 7, 9, 11, 13]
print(binary_search(data, 14))
