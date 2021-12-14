#!/usr/bin/env python3

import sys


def is_valid(comma_sep_str):
  if ';' in comma_sep_str or ',,' in comma_sep_str or ' ' in comma_sep_str:
    return 'Not valid'
  else:
    return 'Valid'
        
def check_series():
  for line in sys.stdin:
    line = str(line)
    if is_valid(line) == "Valid" and len(line.strip().split(",")) == 4:
      data = line.strip().split(",")
      timestamp, city, item, cost = data
      print(city + "," + cost)

if __name__ == "__main__":
	check_series()
