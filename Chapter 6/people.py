user_0 = {
    'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
}
user_1 = {
    'username':'wizard_woz',
    'first':'wizard',
    'last':'woz'
}


people = [user_0,user_1,]
user_2 = {
     'username':'famoss',
     'first':'fafa',
     'last':'moss',
     }
people.append(user_2)
for person in people:
    if person['username']=='efermi':
        person['username'] = 'MR10'
        person['first'] = 'marcus'
        person['last'] = 'rashford'

for person in people[:2]:
    print(person)


print(f"The length of the list is: {len(people)}")