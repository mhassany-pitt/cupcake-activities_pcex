#Step 1: Read the milliseconds
text = input("Enter the milliseconds: ")
milliseconds = int(text)
#Step 2: Obtain hours, minutes, and seconds from the milliseconds
total_secs = milliseconds // 1000
hours = total_secs // 3600
mins = ( total_secs // 60 ) % 60
secs = total_secs % 60
#Step 3: Display the result
print(milliseconds, "milliseconds is", hours, "hours and" , mins , "minutes and" , secs , "seconds.")
