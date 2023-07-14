class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}:" \
               f" {self.content}. Sent: {self.is_sent}"


# Read user input
data = input()

# Variables
emails = []

# Logic
while data != "Stop":
    sender1, receiver1, content1 = data.split()
    email = Email(sender1, receiver1, content1)
    emails.append(email)
    data = input()

sent_emails_indices = [int(x) for x in input().split(", ")]

for index in sent_emails_indices:
    emails[index].send()
# End of Logic

# Print Output
[print(x.get_info()) for x in emails]
