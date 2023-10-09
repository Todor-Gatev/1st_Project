import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


MIN_LENGTH = 5
VALID_DOMAINS = (".com", ".bg", ".net", ".org")

regex_domain = re.compile(r'\.[a-z]+')

email = input()

while email != "End":
    if "@" not in email or email.count("@") > 1:
        raise MustContainAtSymbolError("Email should contain exactly one @ symbol!")
    if len(email.split("@")[0]) < MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if regex_domain.findall(email)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
