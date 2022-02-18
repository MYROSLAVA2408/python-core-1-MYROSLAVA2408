def sum_even_nums_in_range(start, stop):

  count = 0
  for x in range(start, stop):
            if x % 2 == 0:
              count += x
  return count


print(sum_even_nums_in_range(4, 13))
print(sum_even_nums_in_range(1, 9))




