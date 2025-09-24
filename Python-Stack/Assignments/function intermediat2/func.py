x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print(z)




students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for el in students:
    for key,value in el.items():
        print(f"{key} - {value} ")

def itreat(student):

    for k in range(len(student)):
        print(student[k]["first_name"])
        

itreat(students)

def itreat(student):

    for k in range(len(student)):
        print(student[k]["last_name"])
        
itreat(students)


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print()
print()

def printInfo(some_dict):
    length = len(some_dict["locations"])
    print(str(length)+["locations"])
    for i in some_dict(["locations"]):
        print(i)
    print()
    length2 = len(some_dict['instructors'])
    print(str(length2)+ " INSTRUCTORS" )
    for i in some_dict['instructors']:
        print(i)
printInfo(dojo)