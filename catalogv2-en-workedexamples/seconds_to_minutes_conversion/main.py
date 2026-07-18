#Step 1: Read the seconds
text = input("Enter an integer for seconds: ")
seconds = int(text)
#Step 2: Obtain minutes and remaining seconds from the input seconds
minutes = seconds // 60
remaining_seconds = seconds % 60
#Step 3: Display the result
print(seconds , "seconds is" , minutes , "minutes and" , remaining_seconds , "seconds.")
