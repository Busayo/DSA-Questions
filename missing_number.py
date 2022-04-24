
def missing_number(input):
  n = len(input) + 1
  current_sum = sum(input)
  actual_sum = ((n * (n +1)) / 2)
  
  missing_digit = actual_sum - current_sum
  return missing_digit

input = [3, 7, 1, 2, 8, 4, 5]
print(missing_number(input))