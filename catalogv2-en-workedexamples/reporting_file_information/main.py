#Step 1: Define the function
def get_stat(file_name):
        #Step 1.1: Assign initial value to variable that we need for reporting the file information
        num_lines = 0
        longest_line = ""
        #Step 1.2: Enclose the code that might throw an exception within the try block
        try :
                #Step 1.2.1: Open the file and process each line in the file
                myfile = open( file_name, "r")
                for line in myfile:
                        num_lines += 1
                        num_words = len(line.split())
                        #Determine if the line is the longest line so far
                        if (len(line) > len(longest_line)) :
                                longest_line = line
                        #Find the length of the longest word in the line
                        longest_word = 0
                        for w in line.split() :
                                if len(w) > longest_word :
                                        longest_word = len(w)
                        #Print the line information
                        print("Line " + str(num_lines) + " has " + str(num_words) + " tokens (longest = " + str(longest_word) + ")")
                print("Longest line:" + longest_line)
                #Step 1.2.2: Close the file
                myfile.close()
        #Step 1.3: Handle all possible exceptions that may be thrown in the try block
        except FileNotFoundError:
                print("File not found.")
        except IOError:
                print("Problem with the file!")
#Step 2: Call the function
name = input("Enter the full path of a file: " )
get_stat( name )
