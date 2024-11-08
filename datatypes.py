number = 25
second = 56.78
text = "Hello there"
isPythonInteresting = True

print(number)
print(second)
print(text)
print(isPythonInteresting)

print(type(number))
print(type(second))
print(type(text))
print(type(isPythonInteresting))

skates = ["roller", "tri", "speedboots", "rollerblades", "skateboards"]
# Lists: elements are ordered and changeable
print(skates)
print(type(skates))

skaters = ("Joe", "JJ", "Steph", "Jim", "Sam", "Januaries")
# Tuples are ordered but unchangeable
print(skaters)
print(type(skaters))

countries = {"Kenya", "Tanzania", "Uganda"}
print(countries)
print(type(countries))
# Set Elements are unordered and immutable;unchangeable

student = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "major": "Psychology",
    "nationality": "Kenya"
}
print(student)
print(type(student))
print(student["first_name"])
print(student["last_name"])
print(student["age"])
print(student["major"])
print(student["nationality"])

# Typecasting: converting a data type to another
print(float(number))
print(int(second))
print(str(isPythonInteresting))


