#Step 1: Receive the values for each side of a right-angle triangle
text = input("Enter the length of side A:")
side_A = float(text)
text = input("Enter the length of side B:")
side_B = float(text)
#Step 2: Calculate square of side A
squareside_A = side_A ** 2
#Step 3: Calculate square of side B
squareside_B = side_B ** 2
#Step 4: Use Pythagorean theorem to calculate the length of the triangle's hypotenuse
hypotenuse = ( squareside_A + squareside_B ) ** 0.5
#Step 5: Print the result
print("Given that side A is", side_A, "and side B is", side_B, ", the hypotenuse is", hypotenuse)
