# Step 1: Define the function
def binary_search(data, key, low, high):
        # Step 1.1: Set default values
        guess = (high + low) // 2
        # Step 1.2: Set terminating condition(s)
        if low >= high:
                return -1
        elif key == data[guess]:
                return data.index(key)
        # Step 1.3: Set recursion condition
        else:
                if (key < data[guess]):
                        high = guess
                else:
                        low = guess + 1
                return binary_search(data, key, low, high)
# Step 2: Test the function
List = [2,4,8,15,19,20,22,29,31,35,38]
key = 5
idx = binary_search(List, key, 0, len(List))
print(idx)
