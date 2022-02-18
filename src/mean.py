def mean(number):
  sum = 0
  while number > 0:
    sum += number % 10
    number = number//10
  return sum // 2


print(mean(42))
print(mean(64))
print(mean(79))