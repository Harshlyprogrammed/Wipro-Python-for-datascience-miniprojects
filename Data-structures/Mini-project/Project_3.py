students = {
    "homi bhabha":[98,99,97],
    "MK Gandhi":[45,78,53],
    "Narendra Modi":[23,33,46]
}

name = input("enter the name of the student : ")

marks = students[name]
average = sum(marks)/len(marks)

print("the average marks are : ",average)