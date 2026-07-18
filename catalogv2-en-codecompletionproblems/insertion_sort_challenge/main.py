# Define the insertion sorting function that sorts the given list in a descending order
def insertion_sort(data):
        for i in range(1, len(data)):
                current = data[i]
                j = i-1
                while j>=0 and current > data[j]:
                        data[j+1] = data[j]
                        j -=1
                data[j+1] = current
        return data
num_list = [30, -20, 25, 0, 2, 5]
print(insertion_sort(num_list))
