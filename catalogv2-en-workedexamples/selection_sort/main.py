# Define a function that achieves ascending-order selection sort.
def sel_sort(data):
        # Reorder the list in an ascending order.
        for i in range(len(data)):
                min_index = i
                for j in range(i+1, len(data)):
                        if data[min_index] > data[j]:
                                        min_index = j
                data[i], data[min_index] = data[min_index], data[i]
        return data
num_list = [20, -3, 0, 25, 300, 10]
print(sel_sort(num_list))
