
# dictionary1 = {
#   "name": "ABC",
#   "age":25,
#   "salary": 15000,
#   "city": "Rajkot"
 
# }
# keysToRemove = ["name", "salary"]

# Check if a value 200 exists in a dictionary

# dictionary1 = {'a': 100, 'b': 200, 'c': 300}

dictionary1 = {
  "name": "ABC",
  "age":25,
  "salary": 15000,
  "city": "Rajkot"
}

dictionary1.pop("name")
dictionary1.pop("salary")
print(dictionary1)


dictionary2 = {'a': 100, 'b': 200, 'c': 300}
x = input("enter to find value  in dictionary :")
if (x in dictionary2.values()):
    print("in the dictinary")
else:
    print("not in dictionary")

dictionary1.has_key("name") 