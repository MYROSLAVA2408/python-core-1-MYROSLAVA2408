def fizz_buzz(param):
  if param % 3 == 0:
    result = 'fizz'
  if param % 5 == 0:
    result = 'buzz'
  if param % 3 == 0 and param % 5 == 0:
    result = 'fizz_buzz'
  if param % 3 != 0 and param % 5 != 0:
    result = str(param)

  return result

print(fizz_buzz(10))
print(fizz_buzz(9))
print(fizz_buzz(1))


