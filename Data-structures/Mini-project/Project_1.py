person = {"rahul":"very good at maths", "dev":"plays awesome football", "ravi":"just a dumb guy,igonore him!"}

for key,value in person.items():
    print(key,":", value)

person["dev"]="now he cannot plays football"
person["ram"]="topper in everything"

print()
for key,value in person.items():
    print(key,":", value)