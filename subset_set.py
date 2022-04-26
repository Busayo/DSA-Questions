

def subset(nums):
  n = len(nums)
  output = [[]]
  
  for num in nums:
    output += [curr + [num] for curr in output]
    
  return output


nums = [2, 3, 4]
print(subset(nums))