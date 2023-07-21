title = input()
article = input()
print(f"<h1>\n\t{title}\n</h1>")
print(f"<article>\n\t{article}\n</article>")

command = input()

while command != "end of comments":
    print(f"<div>\n\t{command}\n</div>")
    command = input()

