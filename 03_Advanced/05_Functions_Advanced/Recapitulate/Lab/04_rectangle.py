def rectangle(length: int, width: int):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f"Rectangle area: {area()}\n" \
           f"Rectangle perimeter: {perimeter()}"


print(rectangle(2, 10))  # Rectangle area: 20 new row Rectangle perimeter: 24
print(rectangle('2', 10))  # Enter valid values!
