#Step 1: Receive the values for the first side of a right-angle triangle and the hypotenuse
text = input("Enter the length of side A:")
side_A = float(text)
text = input("Enter the length of the hypotenuse:")
hypotenuse = float(text)
#Step 2: Calculate square of side A
square_side_A = side_A ** 2
#Step 3: Calculate square of hypotenuse
square_hypotenuse = hypotenuse ** 2
#Step 4: Use Pythagorean theorem to calculate the length of the triangle's other adjacent side
side_B = (square_hypotenuse - square_side_A) ** 0.5
#Step 5: Print the result
print("Given that side A is", side_A, "and the hypotenuse is", hypotenuse, ", side B is", side_B)
