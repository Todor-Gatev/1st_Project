class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass
EMAIL_MIN_LENGHT = 5
VALID_SUB_DOMAINS = ["com", "bg", "org", "net"]
while True:
    command = input()
    if command == "End":
        break
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")
    username, domain = command.split("@")
    if len(username) < EMAIL_MIN_LENGHT:
        raise NameTooShortError("Name must be more than 4 characters")
    sub_domain = domain.split(".")
    if sub_domain[-1] not in VALID_SUB_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid" )
