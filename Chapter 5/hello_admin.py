users = ['woz','moss','leslie','admin','anabelle']
for user in users:
    if user.lower() == "admin":
        print(f"Hello {user.title()} would you like to see the Status report today?")
    else:
        print(f"hello {user.upper()},  thanks for logging in.")
print("Done with this shid")