# .Get the key corresponding to the minimum value from the following dictionary

dictionary1 = {
  'SE': 82,
  'ADA': 65,
  'Python': 75
}

x = dictionary1.values()
x = list(x)
x.sort()
print("minimum value in dictionary is:",x[0])

