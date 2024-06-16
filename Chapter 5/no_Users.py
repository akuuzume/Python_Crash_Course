users = ['woz','moss','leslie','admin','anabelle']
if users:
    for user in users:
        if user.lower() == "admin":
            print(f"Hello {user.title()} would you like to see the Status report today?")
        else:
            print(f"Hello {user.upper()} , thanks for logging in")
else:
    print("We need some fucking users!!")

# I'll come back with more efficient code to remove the users all at a go wai
users.pop() 
users.pop() 
users.pop() 
users.pop() 
users.pop()

if users:
    for user in users:
        if user.lower() == "admin":
            print(f"Hello {user.title()} would you like to see the Status report today?")
        else:
            print(f"Hello {user.upper()} , thanks for logging in")
else:
    print("We need some fucking users!!")