# Step 1: Define the first class containing the comparison method
class A:
        def __init__(self, value):
                self.value = value
        def __eq__(self, other):
                print ("A __eq__ called")
                return self.value == other
# Step 2: Define the second class containing the comparison method
class B:
        def __init__(self, value):
                self.value = value
        def __eq__(self, other):
                print ("B __eq__ called")
                return self.value == other
# Step 3: Test the comparison function
valueA = A(3)
valueB = B(3)
print(valueA==valueB)
