# Keep asking the user for input until they enter a number between 1 and 10.

while True:
    input_num = int(input("Enter a number b/w 1 - 10 to terminate: "))
    
    if  1 <= input_num <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Number")
