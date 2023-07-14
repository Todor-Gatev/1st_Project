class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


command = input()

emails = []

while command != "Stop":
    sender1, receiver1, content1 = command.split()
    email = Email(sender1, receiver1, content1)
    emails.append(email)
    command = input()

indices_of_the_sent_emails = [int(x) for x in input().split(", ")]

for index, email in enumerate(emails):
    if index in indices_of_the_sent_emails:
        email.send()

    print(email.get_info())

# def add_number_12(num_seq):
#     num_seq.append(12)
#
#
# nums = [1, 2, 3]
# print(nums)  # [1, 2, 3]
# add_number_12(nums)  # NO return BUT changed by the function
# print(nums)  # [1, 2, 3, 12]


# word = [1, 2, 3]
# reversed_list = reversed(word)
# reversed_word = "".join(reversed_list)
# print(reversed_word)
# print(word[::-1])

# strings_list = ["1", "2", "3", "4"]
# nums_list = list(map(int, strings_list))
# # nums_list = [int(x) for x in strings_list]
# print(strings_list)
# print(nums_list)

# list_a = ["aa", "bb"]
# list_b = ["cc", "dd"]
# print(list_a + list_b)  # ['aa', 'bb', 'cc', 'dd']
# # print(list_a.extend(list_b))  # None
# # print(list_a)  # ['aa', 'bb', 'cc', 'dd']
# # print(list_a.append(list_b))  # None
# print(list_a)  # ['aa', 'bb', 'cc', 'dd', ['cc', 'dd']]
