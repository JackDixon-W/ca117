#!/usr/bin/env python3


def swap_keys_values(d):
  out = {}
  for keys, values in d.items():
    out[values] = keys
  return out

def main():
  my_dict = {'a' : 4, 'b' : 7, 'c' : 10}
  new_dict = swap_keys_values(my_dict)
  print(sorted(new_dict.items()))

if __name__ == '__main__':
  main()
