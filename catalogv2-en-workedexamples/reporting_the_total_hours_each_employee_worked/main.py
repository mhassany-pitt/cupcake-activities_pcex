#Step 1: Define the function
def report_work_hours(file_name):
        #Step 1.1: Enclose the code that might throw an exception within the try block
        try :
                #Step 1.1.1: Open the file and process each line in the file
                myfile = open( file_name, "r")
                for line in myfile:
                        tokens = line.split()
                        name = tokens[0]
                        total = 0.0;
                        for i in range(1, len(tokens)) :
                                try :
                                        total += float(tokens[i])
                                except ValueError:
                                        print("Error in the hour.")
                        print("Total hours worked by " + name  + " = " + str(total))
                #Step 1.1.2: Close the file
                myfile.close()
        #Step 1.2: Handle all possible exceptions that may be thrown in the try block
        except FileNotFoundError:
                print("File not found")
        except IOError:
                print("Problem with the file!")
#Step 2: Call the function
name = input("Enter the full path of a file: ")
report_work_hours(name)
