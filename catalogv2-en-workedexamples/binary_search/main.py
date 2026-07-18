# Define a binary search function
def binary_search(data, key):
        found = False
        low = 0
        high = len(data)-1
        while not found:
                guess = (high+low)//2
                if (key == data[guess]):
                        found = True
                else:
                        if (key<data[guess]):
                                high = guess-1
                        else:
                                low = guess+1
        return guess
data = [1, 5, 7, 9, 11, 13]
print(binary_search(data, 13))
