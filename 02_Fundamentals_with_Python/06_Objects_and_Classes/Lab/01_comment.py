class Comment:
    def __init__(self, first_name1, last_name, age=0):
        self.username = first_name1
        self.content = last_name
        self.likes = age


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)
comment.username = 23
print(comment.username)
print(comment.content)
