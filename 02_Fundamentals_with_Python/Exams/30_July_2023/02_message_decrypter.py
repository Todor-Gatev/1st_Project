import re

regex = re.compile(r"^([$%])(?P<tag>[A-Z][a-z]{2,})\1:\s\[(?P<num1>\d+)]\|\[(?P<num2>\d+)]\|\[(?P<num3>\d+)]\|$")

# Logic
for _ in range(int(input())):
    text = input()
    res = regex.match(text)

    if res:
        ch1 = chr(int(res.group("num1")))
        ch2 = chr(int(res.group("num2")))
        ch3 = chr(int(res.group("num3")))
        print(f"{res.group('tag')}: {ch1}{ch2}{ch3}")
    else:
        print("Valid message not found!")
# End of Logic
