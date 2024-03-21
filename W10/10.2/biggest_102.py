def biggest(inp):
  if len(inp) == 1:
    return inp[0]
  else:
    big = biggest(inp[1:])
    first = inp[0]
    if first > big:
      big = first
    return big

