# todo:
# give user 2 choices "Login" or "Register"
# if register, get username from user, store the username in a file
# if login, get username from user and check if the name exist in the file



file_path = "day_12/assgfile.txt"

choice = input("Choose an option: Login (L) or Register (R)(L/R): ").strip().upper()

if choice == "R":
    username = input("Enter a username to register: ")

    f = open(file_path, "a")   # open file in append mode
    f.write(username + "\n")   # write username
    f.close()                  # close file

    print("User registered successfully!")

elif choice == "L":
    username = input("Enter your username to login: ")

    try:
        f = open(file_path, "r")   # open file in read mode
        users = f.read()           #read the file
        f.close()

        if username in users:
            print("Login successful! Welcome", username)
        else:
            print(" Username not found. Please register.")

    except FileNotFoundError:
        print(" User file missing. Please register first.")

else:
    print("Invalid choice! Enter L or R.")

