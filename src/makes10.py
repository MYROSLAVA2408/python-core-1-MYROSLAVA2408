def makes10(a, b):
  if a == 10:
    result = True
  elif b == 10:
    result = True
  elif a + b == 10:
    result = True
  else:
    result = False
  return result

print(makes10(4, 10))
print(makes10(4, 1))
print(makes10(4, 6))