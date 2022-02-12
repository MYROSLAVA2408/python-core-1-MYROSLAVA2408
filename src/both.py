def both(number1, number2):
  if number1 == 0 and number2 == 0:
    result = 'True'
  elif number1 > 0 and number2 > 0:
    result = 'True'
  elif number1 < 0 and number2 < 0:
    result = 'True'
  else:
    result = 'False'
  return result

print(both(3,0))
print(both(0,0))
print(both(3,6))
