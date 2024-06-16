mammals = ['dog','cat','panda','rabbit','bear','kangaroo']
print("The first three elements in this list are: ")
for mammal in mammals[:3]:
    print(mammal)
print("Three items from the middle of the list are:")
for mammal in mammals[2:-1]:
    print(mammal)
print("The last three items in the list are:")
for mammal in mammals[-3:]:
    print(mammal)