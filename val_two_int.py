

def array_sum(set_array, value):
  store_set = set()
  for i in set_array:
    if value - i in store_set:
      return True
    store_set.add(i)
  
  return False
  
  
  
set_array = (5, 7, 1, 2, 8, 4, 3)
value = 5
print(array_sum(set_array, value))