"""
Take the list
smallest can only take list inputs
If the number at the start of the list is less than the number
returned by the function itself
"""
def smallest(inp):
  if len(inp) == 1:
    return inp[0]
  else:
    small = smallest(inp[1:])
    first = inp[0]
    if first < small:
      small = first
    return small

