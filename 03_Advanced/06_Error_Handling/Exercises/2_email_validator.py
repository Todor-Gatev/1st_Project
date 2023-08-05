import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


allowed_domains = {"com", "bg", "net", "org"}
regex = re.compile(r"[^@]{5,}@[^@.]+\.(?P<domain>[^@]+)")

while True:
    checked_email = input()

    if checked_email == "End":
        break

    result = regex.match(checked_email)

    if result:
        if result.group("domain") in allowed_domains:
            print("Email is valid")
        else:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        if '@' not in checked_email:
            raise MustContainAtSymbolError


# NameTooShortError - raise it when the name in the email is less than or equal to 4
# ("peter" will be the name in the email "peter@gmail.com")
# MustContainAtSymbolError - raise it when there is no "@" in the email
# InvalidDomainError - raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
#
# When an error is encountered, raise it with an appropriate message:
# NameTooShortError - "Name must be more than 4 characters"
# MustContainAtSymbolError - "Email must contain @"
# InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
#
# Hint: use the following syntax to add a message to the Exception: MyException("Exception Message")
# If the current email is valid, print "Email is valid" and read the next one
