
''' Returns true if a binary tree is a binary search tree '''


def wordBreak(word, dictionary):
  for i in range(1, len(word) + 1):
    first = word[0:i]
    if first in dictionary:
      second = word[i:]
      if not second or second in dictionary or wordBreak(second, dictionary):
        return True
  return False


word = "hellonow"
dictionary = set(["hello", "hell", "on", "now"])
if wordBreak(word, dictionary):
  print("String Can be Segmented")
else:
  print("String Can NOT be Segmented")


