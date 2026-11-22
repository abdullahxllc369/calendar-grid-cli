"""Print a Monday-first month calendar."""
import argparse
import calendar

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('year', type=int)
p.add_argument('month', type=int, choices=range(1, 13))
a = p.parse_args()

print(calendar.month(a.year, a.month), end='')
