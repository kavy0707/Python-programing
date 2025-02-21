#  Create a new dictionary by extracting the following keys from a given dictionary

# dictionary1 = {
#   "name": "abc",
#   "age":25,
#   "salary": 15000,
#   "city": "Rajkot"
 
# }

# Keys to extract

# keys = ["name", "salary"]


dictionary1 = {
  "name": "abc",
  "age":25,
  "salary": 15000,
  "city": "Rajkot"
}
x = dictionary1["name"]
y = dictionary1.get("salary")

dictionary2 = {
    "name" : x,
    "salary" : y
}

print(dictionary2)