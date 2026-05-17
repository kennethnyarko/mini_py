
student = {
    "name": "Ama",
    "age": 20,
    "course": "Computer Science",
    "grade": "B+"}

student.update({'grade' : 'A'})

#adding new key value pair
student['city']= 'Accra'

#remove key value pair
student.pop('age') 
        
#loop through the dictionary / BRING WHATEVER IS IN A DICTIONARY(keys are the main names [name,age]and values are the content [24,kofi])
for key ,value in student.items():
    print(key, value)