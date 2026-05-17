notes_text = """🧠 Python Dictionaries — Course Notes (Step-by-Step)
📌 What is a Dictionary?

A dictionary in Python is a collection that stores data in key-value pairs.

📖 Explanation:
A key is like a label (e.g. "name")
A value is the data stored under that label (e.g. "John")

Example structure:

key: value
📌 1. Creating a Dictionary
Given Example:
students = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
🧠 Explanation:

We are creating a dictionary called students that stores:

"name" → "John"
"age" → 25
"courses" → ['Math', 'CompSci'] (a list inside a dictionary)

👉 This is how we store structured real-life data like student records.

📌 2. Accessing Data from a Dictionary
Code:
print(students['name'])
print(students['age'])
print(students['courses'])
🔹 Accessing Name
print(students['name'])

📖 Explanation:

We use the key "name" to get its value from the dictionary.

✅ Output:
John
🔹 Accessing Age
print(students['age'])
📖 Explanation:

We access the key "age" and Python returns 25.

✅ Output:
25
🔹 Accessing Courses
print(students['courses'])
📖 Explanation:

The key "courses" contains a list of subjects, so Python prints the whole list.

✅ Output:
['Math', 'CompSci']


📌 3. Updating Dictionary Values (Corey Schafer concept)
🧠 Explanation:

Dictionaries are mutable, meaning we can change values.

Example:
students['age'] = 26

👉 This updates age from 25 → 26


📌 4. Adding New Key-Value Pairs
Example:
students['city'] = 'Accra'
📖 Explanation:

We are adding a new field called "city".

📌 5. Deleting Key-Value Pairs
Example:
del students['age']
📖 Explanation:

This removes the "age" key completely from the dictionary.

📌 6. Looping Through a Dictionary (Efficient Access)
🔹 Loop through keys and values:
for key, value in students.items():
    print(key, value)
📖 Explanation:
.items() gives both key and value
We loop through the whole dictionary efficiently
✅ Output:
name John
age 25
courses ['Math', 'CompSci']
📌 7. FULL STEP-BY-STEP SOLUTION OF YOUR CODE
Given:
students = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(students['name'])
print(students['age'])
print(students['courses'])
🧠 Step-by-step Explanation:
Step 1: Dictionary is created

We store student data in key-value format.

Step 2: Access "name"
students['name']

👉 Python looks for key "name" → returns "John"

Step 3: Access "age"
students['age']

👉 Returns 25

Step 4: Access "courses"
students['courses']

👉 Returns list:

['Math', 'CompSci']
✅ Final Output:
John
25
['Math', 'CompSci']
🧠 KEY TAKEAWAYS
Dictionaries store data as key → value pairs

Access values using:

dictionary['key']"""
