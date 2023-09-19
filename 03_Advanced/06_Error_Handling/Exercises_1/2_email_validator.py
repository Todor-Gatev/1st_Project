import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


allowed_domains = {"com", "bg", "net", "org"}
regex = re.compile(r"\w{5,}@[^@.]+(\.(?P<domain>[^@.]+))+")  # according to exercise requirements
# regex = re.compile(r"(?:^|(?<=\s))[a-z0-9]+(?:[-._][a-z0-9]+)*@[a-z]+(?:-[a-z]+)*(?:\.[a-z]+)+(?:$|(?=[.,\s]))")
name_regex = re.compile(r"\w{5,}")

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
        if not name_regex.match(checked_email):
            raise NameTooShortError("Name must be more than 4 characters "
                                    "and can contain only letters, digits and underscores!")
        elif checked_email.count('@') != 1:
            raise MustContainAtSymbolError("Email must contain exactly one @")
        else:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

# peter@gmail.net.aus.com    peter@gmail.com  pete@hotmail.com
