# Define a function that achieves descending-order selection sort.
def sel_sort(data):
        for i in range(len(data)):
                        max_index = i
                        for j in range(i+1, len(data)):
                        # Check if the current element at maxindex is smaller than the next element
                                if data[max_index] < data[j]:
                                        max_index = j
                        data[i], data[max_index] = data[max_index], data[i]
        return data
num_list = [20, -3, 0, 25, 300, 10]
print(sel_sort(num_list))
