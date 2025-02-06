courses = ["MIT","Cyber security ", "datascience"]
print(courses)

# Accessing an element
print( courses[2])

# looping through an array
for a in courses:
    print("course",a)


# adding a new element into an array
courses.append("laravel")
print(courses)

#deleting an element from an array
courses.remove("cyber security")
print(courses)
