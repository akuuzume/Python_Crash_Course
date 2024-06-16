favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edem': 'java',
 'phil': 'python',
 }
to_take_poll_names = ['edem','kofi','fafa','sarah']

for names in favorite_languages.keys():
    if names in to_take_poll_names:
        print(f"Thanks for thanking the poll,{names.title()}.")
    else:
        print(f"{names.title()}, please take our poll.")


