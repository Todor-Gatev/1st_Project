
from math import floor

total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

pages_per_day = total_pages / days
hours_per_day = floor(pages_per_day / pages_per_hour)
print(hours_per_day)

