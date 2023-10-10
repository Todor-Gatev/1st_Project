class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


USERNAME_MIN_LENGHT = 4
DOMAINS = [".com", ".bg", ".org", ".net"]

email = input()

while email != "End":
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    
    username = email.split("@")[0]
    
    if len(username) <= USERNAME_MIN_LENGHT:
        raise NameTooShortError("Name must be more than 4 characters")
    
    domain = "." + email.split(".")[-1]
    
    if domain not in DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    
    print("Email is valid")
    email = input()
