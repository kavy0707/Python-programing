# Rename key city to location in the following dictionary

dictionary1 = {
  "name": "ABC",
  "age":25,
  "salary": 15000,
  "city": "Rajkot"
}

x = dictionary1.get("city")
dictionary1.pop("city")

dictionary1["location"]= x
print(dictionary1)