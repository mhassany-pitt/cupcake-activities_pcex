#Step 1: Define the function
def concat_chars(a, b):
        new_a = b[:2] + a[2:]
        new_b = a[:2] + b[2:]
        return (new_a + " " + new_b)
#Step 2: Call the function
print(concat_chars("Hello", "There"))
