def int_within_bounds(number, lower_bound, upper_bound):
  if number >= lower_bound and number < upper_bound:
    result = 'true'
  if not  (number >= lower_bound and number < upper_bound):
      result = 'foulse'
  if number % 1 != 0:
    result = 'faulse'
  return result

print(int_within_bounds(2, 1, 4))
print(int_within_bounds(2.7, 1, 4))
print(int_within_bounds(5, 1, 4))