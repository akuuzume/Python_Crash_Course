current_users = ['wizard','woz','thor','bortos']
new_users = ['ThoR','woz','yakubu','moss','fafa']

for users in new_users:
    if users.lower() in current_users:
        print(f"{users}, you would need to use a new username")
    