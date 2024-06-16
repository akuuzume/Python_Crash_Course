programming_Buzzwords = {
    'in':'to check if something exists within a list',
    'not':'the negation of a function',
    'tuple':'an immutable or unchangeable list',
    "list":"a collection of like items",
    'range':'a function that helps you generate values from a start index to a just before a stop index',
    'keys': 'to pull the keys from a dictionary',
    'set':'to avoid duplicates of values of a dictionary'

}

print("****** Welcome to the Programming whiz words world *******")
print("Words \t\t Meanings")
for keys,values in programming_Buzzwords.items():
    print(f"{keys.lower()}: \t\t{values.title()}")