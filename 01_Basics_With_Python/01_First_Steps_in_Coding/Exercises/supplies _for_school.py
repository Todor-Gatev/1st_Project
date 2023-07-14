
pen_packages = int(input())
marker_packages = int(input())
cleaner_litres = int(input())
discount = int(input())

pen_price = pen_packages * 5.80
marker_price = marker_packages * 7.20
cleaner_price = cleaner_litres * 1.20

price = pen_price + marker_price + cleaner_price
final_price = price * (1 - discount / 100)
print(final_price)
